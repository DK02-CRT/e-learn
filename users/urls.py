from django.urls import path
from .views import signin, acccount, signout, signup

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('account/', acccount, name='account'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),

]