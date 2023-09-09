from django.db import models

from constans import NULLABLE


class Payment(models.Model):
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='date_of_payment')
    course_paid = models.ForeignKey('academy.Course', **NULLABLE, on_delete=models.CASCADE, verbose_name='course_paid')
    lesson_paid = models.ForeignKey('academy.Lesson', **NULLABLE, on_delete=models.CASCADE, verbose_name='lesson_paid')
    payment_method = models.CharField(max_length=150, choices=[('cach', 'Cach'), ('transfer', 'Transfer')], verbose_name ='payment_amount')
    payment_amount = models.IntegerField(verbose_name='payment_amount')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user', related_name='payments')
