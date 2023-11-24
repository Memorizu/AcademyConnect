
from rest_framework import serializers

from academy.models import Course
from academy.models.lesson import Lesson
from academy.validators import UrlValidator
from constans import NOW
from users.models import User
from academy.tasks import send_course_update_email


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

        difference_time = NOW - course.updated_at

        if difference_time.total_seconds() > 4 * 3600:
            send_course_update_email.delay(course.id)
        course.updated_at = NOW
        course.save()

        return super().update(instance, validated_data)
