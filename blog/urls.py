from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
]

'''
FBV = Function Based View
코드를 많이 짜야한다.
섬세하게

CBV = Class Based View
편해
섬세하게 -> 함수

'''