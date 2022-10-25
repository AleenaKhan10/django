from django.urls import path
from . import views

urlpatterns = [
    path('alina/', views.say_hello)
]