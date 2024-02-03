from django.urls import path, include
from .views import *

urlpatterns = [
    path('Application/', Application, name='Application')
]