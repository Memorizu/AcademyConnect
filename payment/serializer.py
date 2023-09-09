from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = (
            'id',
            'date_of_payment',
            'course_paid',
            'lesson_paid',
            'payment_method',
            'payment_amount',
            'user'
        )
