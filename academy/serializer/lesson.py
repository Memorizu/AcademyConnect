from rest_framework import serializers

from academy.models import Course
from academy.models.lesson import Lesson
from users.models import User


class LessonCreateSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course', 'user')


class LessonViewSerializer(LessonCreateSerializer):
    course = serializers.StringRelatedField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course', 'user')
