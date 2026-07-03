from django.urls import path
from .views import courses, module_detail, topic_detail

urlpatterns = [
    path('', courses, name='courses'),
    path('<int:pk>/', module_detail, name='module_detail'),
    path('<int:module_pk>/<int:topic_pk>/', topic_detail, name='topic_detail'),
]
