from django.urls import path
from .views import course_detail
from .views import topic_detail

urlpatterns = [
    path('<slug:slug>/', course_detail, name='course_detail'),
    path('topic/<int:pk>/', topic_detail, name='topic_detail'),
]