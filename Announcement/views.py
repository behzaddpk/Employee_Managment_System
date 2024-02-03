from django.shortcuts import render
from .models import *
from django.contrib import messages 
import datetime
from django.db.models import Q

# Create your views here.
def Announcements(request):
    data = Announcement.objects.all()
    if request.method == 'POST':
        announce = request.POST.get('searchannouncement')
        if announce:
            print(announce)
            data = Announcement.objects.filter(Q(title__icontains=announce))

    return render(request, 'Announcement.html', {'data': data})

def AnnouncementForms(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('Paragraph')
        announcement = Announcement(title=title, content=content)
        announcement.save()
        messages.success(request, "Announcement Add Successfully.")
    
    return render(request, 'AnnouncementForm.html')


def AnnouncementDetails(request, slug):
    detail = Announcement.objects.get(slug=slug)
    return render(request, 'AnnouncementDetail.html', {'detail': detail})