from django.urls import path, include
from .views import home, health_check

urlpatterns = [
    path('', home, name='home'),
    path('courses/', include('coureses.urls')),
    path('health_check/', health_check, name='health_chech')
]
