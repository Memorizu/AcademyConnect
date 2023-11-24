from django.urls import reverse
from rest_framework import status
from academy.models import Subscription
from academy.tests.base import BaseTestCase


class TestSubscription(BaseTestCase):

    def test_create_subscription(self):
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }

        sub_create = reverse('academy:subscription_create')
        response = self.client.post(sub_create, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_subscription(self):
        Subscription.objects.create(
            id=5,
            user=self.user,
            course=self.course,
            is_active=True
        )

        data = {
            "user": self.user.id,
            "course": self.course.id,
            "is_active": False
        }

        sub_update = reverse('academy:subscription_destroy', kwargs={'pk': 5})
        response = self.client.patch(sub_update, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(data['is_active'])
