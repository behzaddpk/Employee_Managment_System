from django.urls import path
from .views import *

urlpatterns = [
    path('TeamLeaderDashboard', TeamLeaderDashboard, name='TeamLeaderDashboard'),
    path('TeamLeaderList/', TeamLeaderList, name='TeamLeaderList'),
    path('TeamLeaderProfile/<slug:slug>/', TeamLeader_Profile, name='TeamLeaderProfile')
]