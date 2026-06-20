from django.urls import path
from .views import quizes, quiz_detail

urlpatterns = [
    path('', quizes, name='quizes'),
    path('<int:pk>/', quiz_detail, name='quiz_detail'),
]