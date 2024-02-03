from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Announcement)
# class AnnouncementAdmin(admin.ModelAdmin):
#     list_display = ['title', 'content', 'created_at']

