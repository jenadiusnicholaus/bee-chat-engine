from rest_framework import serializers
from .models import UserIntergrationApp  , Payment

class IntegrationAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIntergrationApp
        fields = [
            'id',
            'name',
            'description',
            'user',
            "payment",
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
       

class GetIntegrationAppSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    
    class Meta:
        model = UserIntergrationApp
        fields = [
            'id',
            'name',
            'description',
            'user',
            "payment",
        ]