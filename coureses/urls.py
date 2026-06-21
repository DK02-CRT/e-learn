from django.urls import path
from .views import courses, topic_detail

urlpatterns = [
    path('', courses, name='courses'),
    # path('<slug:slug>/', course_detail, name='course_detail'),
    path('topic/<int:pk>/', topic_detail, name='topic_detail'),
]