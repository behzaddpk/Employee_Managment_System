from django.urls import path
from .views import *

urlpatterns = [
    path('Announcements/', Announcements, name="Announcements"),
    path('AnnouncementForms/', AnnouncementForms, name="AnnouncementForms"),
    path('AnnouncementDetails/<slug:slug>/', AnnouncementDetails, name="AnnouncementDetails")
    
]
