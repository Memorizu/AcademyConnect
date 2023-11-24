
import os

import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import Payment
from payment.serializer import PaymentSerializer
from payment.services import StripePayment


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_method', 'course_paid', 'lesson_paid')
    ordering_fields = ['date_of_payment']


class PaymentCreateAPIView(generics.CreateAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        payment_data = request.data
        payment_serializer = self.get_serializer(data=payment_data)

        if payment_serializer.is_valid():
            payment_serializer.save()
            # payment_id = payment_serializer.data['id']

            stripe_handler = StripePayment(
                paid_object=payment_data.get('course_paid', payment_data.get('lesson_paid')),
                payment_method=payment_data.get('payment_method'),
                payment_amount=payment_data.get('payment_amount')
            )
            try:
                stripe_id = stripe_handler.create()
                payment_serializer.instance.stripe_id = stripe_id
                payment_serializer.instance.save()
                return Response(payment_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentRetrieveAPIView(APIView):

    def get(self, request, pk):
        try:
            payment = get_object_or_404(Payment, pk=pk)
            stripe_id = payment.stripe_id
            stripe.api_key = os.getenv('STRIPE_KEY')
            payment_intent = StripePayment.retrieve(stripe_id)
            return Response(payment_intent, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

