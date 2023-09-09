from rest_framework import serializers

from academy.models.lesson import Lesson


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()

    class Meta:
        model = Lesson
        fields = '__all__'
