from rest_framework import serializers

from payment.serializer import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'payments')


class AdminSerializer(UserSerializer):
    class Meta:
        model = User
        fields = '__all__'
