from django.urls import path

from account import apis as api

urlpatterns = [path("login", api.LoginAPIView.as_view(), name="login")]
