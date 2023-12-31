from django.urls import path
from rest_framework.routers import DefaultRouter
from academy.apps import AcademyConfig
from academy.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionUpdateAPIView

app_name = AcademyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('subscription', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/update/<int:pk>', SubscriptionUpdateAPIView.as_view(), name='subscription_destroy'),
] + router.urls
