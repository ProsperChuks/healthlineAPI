from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CheckoutViewSet(viewsets.ModelViewSet):

    queryset = Checkouts.objects.all()
    serializer_class = CheckoutSerializer
