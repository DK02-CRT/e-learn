from django.urls import path
from .views import signin, acccount, signout

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('account/', acccount, name='account'),
    path('signout/', signout, name='signout')
]