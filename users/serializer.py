from rest_framework import serializers

from payment.serializer import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'payments')

    def create(self, validation_data):
        password = validation_data.pop('password', None)
        user = self.Meta.model(**validation_data)
        user.set_password(password)
        user.save()
        return user


class AdminSerializer(UserSerializer):
    class Meta:
        model = User
        fields = '__all__'
