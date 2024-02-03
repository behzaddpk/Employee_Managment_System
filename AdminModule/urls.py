from django.urls import path, include
from .views import *
from captain.views import *

urlpatterns = [
    path('login/', LOGIN, name='login'),
    path('logout/', LOGOUT, name='logout'),


    path('Staff-register/', StaffRegistration, name='StaffRegistration'),
    path('verify/<auth_token>', verify_partner, name='verify-partner'),
    path('profile/', Profile, name='Profile'),



]
