from rest_framework import serializers
from orders import models

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'