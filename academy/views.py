from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from academy.models.lesson import Lesson
from academy.models.course import Course
from academy.permissions import IsAdmin, IsOwner
from academy.serializer.course import CourseSerializer
from academy.serializer.lesson import LessonCreateSerializer, LessonViewSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        if self.request.user.has_perm('can_view_courses') or self.request.user.is_superuser:
            queryset = self.queryset
        else:
            queryset = Course.objects.filter(user=self.request.user)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        if self.request.user.has_perm('can_view_lessons') or self.request.user.is_superuser:
            return Lesson.objects.all()
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
