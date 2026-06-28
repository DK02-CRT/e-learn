from django.urls import path
from .views import courses, module_detail, topic_detail

urlpatterns = [
    path('', courses, name='courses'),
    path('<slug:slug>/<int:pk>/', module_detail, name='module_detail'),
    path('<slug:slug>/<int:module_pk>/<int:topic_pk>/', topic_detail, name='topic_detail'),
]