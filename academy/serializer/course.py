from rest_framework import serializers

from academy.models.course import Course
from academy.serializer.lesson import LessonViewSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonViewSerializer(read_only=True, many=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'image', 'lessons_count', 'lessons')