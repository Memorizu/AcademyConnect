from django.db import models


class Subscription(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey('academy.Course', on_delete=models.CASCADE, related_name='course_subscriptions')

    def __str__(self):
        return self.is_active

    class Meta:
        verbose_name = 'subscriptions'
        verbose_name_plural = 'subscriptions'
