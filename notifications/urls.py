from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send_qr/', views.send_qr, name='send_qr'),
]
