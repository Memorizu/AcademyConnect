from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from academy.models.lesson import Lesson
from academy.models.course import Course
from academy.permissions import ModeratorPermission, SuperUserPermission
from academy.serializer.course import CourseSerializer
from academy.serializer.lesson import LessonCreateSerializer, LessonViewSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated | ModeratorPermission]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.has_perm('can_view_course'):
            return Course.objects.all()
        return Course.objects.filter(user=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_classes = [ModeratorPermission]


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated | ModeratorPermission]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [ModeratorPermission]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [ModeratorPermission]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [ModeratorPermission]
