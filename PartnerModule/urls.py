from django.urls import path, include
from .views import *


urlpatterns = [
    path('PartnerDashboard/', PartnerDashboard, name='PartnerDashboard'),


    path('Partners/', PartnerList, name='Partners'),
    path('Partners/<slug:slug>/', PartnerProfiles, name='PartnerProfile'),
    
    
]
