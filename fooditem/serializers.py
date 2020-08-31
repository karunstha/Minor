from rest_framework import serializers
from fooditem import models

class FoodItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.FoodItem
        fields = '__all__'