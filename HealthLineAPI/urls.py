from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from phamarcy import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'checkouts', views.CheckoutViewSet, basename='checkout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
