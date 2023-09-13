from rest_framework import serializers

from academy.models import Course
from academy.models.lesson import Lesson


class LessonCreateSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course')


class LessonViewSerializer(LessonCreateSerializer):
    course = serializers.StringRelatedField()
