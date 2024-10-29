
from django.contrib import admin
from django.urls import path,include

from base import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('test_private', views.test_private),

]
