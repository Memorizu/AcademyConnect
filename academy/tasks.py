from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from academy.models import Subscription
from constans import NOW


@shared_task
def send_email(list_of_emails):

    for email in list_of_emails:

        send_mail(
            subject=f'Обновился курс: ',
            message='Посмотрите обновление в курсе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )


# @shared_task
# def send_email_test():
#         send_mail(
#             subject='Обновился курс: {subscription.course}',
#             message='Посмотрите обновление в курсе',
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=['kaidohmary@gmail.com'],
#             fail_silently=False
#         )
