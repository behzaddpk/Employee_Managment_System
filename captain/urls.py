from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from clients.views import *



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', registration, name='register'),
    path('tables/', tables, name='tables'),
    path('charts/', charts, name='charts'),
    path('AddTask/', AddTask, name='AddTask'),
    path('tasklist/', Tasklist, name='Tasklist'),
    path('tasksdescription/<slug:slug>/', TaskDescription, name='TaskDescription'),

    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
