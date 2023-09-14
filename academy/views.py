from rest_framework import viewsets, generics

from academy.models.lesson import Lesson
from academy.models.course import Course
from academy.permissions import OwnerOrModeratorPermission
from academy.serializer.course import CourseSerializer
from academy.serializer.lesson import LessonCreateSerializer, LessonViewSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [OwnerOrModeratorPermission]


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_classes = [OwnerOrModeratorPermission]


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [OwnerOrModeratorPermission]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [OwnerOrModeratorPermission]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [OwnerOrModeratorPermission]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [OwnerOrModeratorPermission]
