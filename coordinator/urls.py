from django.urls import path
from .views import *


urlpatterns = [
    path('CoordinatorDashboard/', CoordinatorDashboard, name='CoordinatorDashboard'),
    path('CoordinatorList/', CoordinatorList, name='CoordinatorList'),
    path('CoordinatorProfile/<slug:slug>/', Coordinator_Profile, name='CoordinatorProfile')
]
