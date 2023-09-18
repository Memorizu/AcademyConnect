from rest_framework import serializers

from academy.models.course import Course
from academy.serializer.lesson import LessonViewSerializer
from academy.serializer.subscription import SubscriptionSerializer, SubscriptionListSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscription = SubscriptionListSerializer(read_only=True, many=True, source='course_subscriptions')
    lessons = LessonViewSerializer(read_only=True, many=True)


    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'image', 'lessons_count', 'lessons', 'subscription')
