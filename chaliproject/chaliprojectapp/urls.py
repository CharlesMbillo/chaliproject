from django.urls import path
from . import views

urlpatterns = [
    path('user_input/', views.user_input, name='user_input'),
]
