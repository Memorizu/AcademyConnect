from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from academy.models.lesson import Lesson
from academy.models.course import Course
from academy.permissions import IsAdmin, IsOwner
from academy.serializer.course import CourseSerializer
from academy.serializer.lesson import LessonCreateSerializer, LessonViewSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lesson.objects.filter(user=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]
