from django.db import models

from constans import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    image = models.ImageField(**NULLABLE, upload_to='courses/', verbose_name='image')
    description = models.TextField(**NULLABLE, verbose_name='description')
    user = models.ForeignKey('users.User', **NULLABLE, on_delete=models.CASCADE, verbose_name='user', related_name='course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
