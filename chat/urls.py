from django.urls import path
from .views import welcome_view, messages_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('messages/', messages_view, name='messages'),
]
