
from rest_framework import serializers

from academy.models import Course, Subscription
from academy.models.lesson import Lesson
from academy.validators import UrlValidator
from constans import NOW
from users.models import User
from academy.tasks import send_email


class LessonCreateSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    link = serializers.URLField(validators=[UrlValidator()])

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course',)


class LessonViewSerializer(LessonCreateSerializer):
    course = serializers.StringRelatedField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course', 'user', 'updated_at')

    def update(self, instance, validated_data):
        instance.updated_at = NOW
        instance.save()
        course = instance.course
        if course:
            course.updated_at = NOW
            course.save()

        subscriptions = Subscription.objects.filter(course=course.id)
        list_of_user_emails = [subscription.user.email for subscription in subscriptions]

        # if subscription.is_active:
        send_email.delay(list_of_user_emails)

        return super().update(instance, validated_data)
