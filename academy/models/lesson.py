from django.db import models

from constans import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='lesson')
    description = models.TextField(**NULLABLE, verbose_name='description')
    preview = models.ImageField(**NULLABLE, upload_to='lessons', verbose_name='preview')
    link = models.URLField(**NULLABLE, verbose_name='link')
    course = models.ForeignKey('academy.Course', on_delete=models.CASCADE, verbose_name='course', related_name='lessons')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user', related_name='lessons')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}{self.course} {self.link}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


