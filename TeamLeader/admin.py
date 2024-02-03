from django.contrib import admin
from django import forms
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.


class TeamLeaderBioForm(forms.ModelForm):
    bio = forms.CharField(widget=TinyMCE())

    class Meta:
        model = TeamLeaderBio
        fields = '__all__'

class TeamLeaderBioInline(admin.StackedInline):
    model = TeamLeaderBio
    form = TeamLeaderBioForm
    extra = 0

class TeamLeaderPhotoInline(admin.StackedInline):
    model = TeamLeaderPhoto
    extra = 0


class TeamLeaderProfileInline(admin.StackedInline):
    model = TeamLeaderProfile
    extra = 0



class TeamLeaderSkillInline(admin.StackedInline):
    model = TeamLeaderSkill
    extra = 0

class TeamLeaderExperienceInline(admin.StackedInline):
    model = TeamLeaderExperience
    extra = 0

class TeamLeaderBankDetailInline(admin.StackedInline):
    model = TeamLeaderBankDetail
    extra = 0


class TeamLeaderEducationInline(admin.StackedInline):
    model = TeamLeaderEducation
    extra = 0



@admin.register(TeamLeaderBio)
class TeamLeaderBioAdmin(admin.ModelAdmin):
    list_display = ['bio',]
    


@admin.register(TeamLeader)
class TeamLeaderAdmin(admin.ModelAdmin):
    inlines = [TeamLeaderPhotoInline, TeamLeaderProfileInline, TeamLeaderBioInline, TeamLeaderSkillInline, TeamLeaderExperienceInline, TeamLeaderBankDetailInline, TeamLeaderEducationInline]
    list_display = ['id',  'team', 'auth_token', 'is_verified', 'is_staff']



