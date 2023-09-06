from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from phamarcy import views

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
