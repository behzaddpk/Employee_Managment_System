from django.urls import path, include
from .views import *


urlpatterns = [
    path('WriterDashboard/', WriterDashboard, name='WriterDashboard'),
    path('WriterList/', WriterList, name='WriterList'),
    path('WriterProfile/<slug:slug>/', Writer_Profile, name='WriterProfile')

]