from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkouts
        fields = '__all__'
