#_*_coding:utf8_*_
from django.urls import path
from aicms import views

urlpatterns = [
    path('', views.index),
]