from datetime import datetime

from rest_framework import serializers

from academy.models import Subscription
from academy.models.course import Course
from academy.serializer.lesson import LessonViewSerializer
from academy.serializer.subscription import SubscriptionListSerializer
from academy.tasks import send_course_update_email
from constans import NOW


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscription = SubscriptionListSerializer(read_only=True, many=True, source='course_subscriptions')
    lessons = LessonViewSerializer(read_only=True, many=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'image', 'lessons_count', 'lessons', 'subscription')

    def update(self, instance, validated_data):
        subscription = Subscription.objects.filter(course_id=instance.id, is_active=True)
        if subscription:
            instance.updated_at = NOW
        send_course_update_email.delay(instance.id)

        instance.save()
        return super().update(instance, validated_data)
