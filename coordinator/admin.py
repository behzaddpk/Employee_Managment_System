from django.contrib import admin
from django import forms
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.


class CoordinatorBioForm(forms.ModelForm):
    bio = forms.CharField(widget=TinyMCE())

    class Meta:
        model = CoordinatorBio
        fields = '__all__'

class CoordinatorBioInline(admin.StackedInline):
    model = CoordinatorBio
    form = CoordinatorBioForm
    extra = 0

class CoordinatorPhotoInline(admin.StackedInline):
    model = CoordinatorPhoto
    extra = 0


class CoordinatorProfileInline(admin.StackedInline):
    model = CoordinatorProfile
    extra = 0

# class CoordinatorBioInline(admin.StackedInline):
#     model = CoordinatorBio
#     list_display = ['bio']
#     extra = 0

class CoordinatorSkillInline(admin.StackedInline):
    model = CoordinatorSkill
    extra = 0

class CoordinatorExperienceInline(admin.StackedInline):
    model = CoordinatorExperience
    extra = 0

class CoordinatorBankDetailInline(admin.StackedInline):
    model = CoordinatorBankDetail
    extra = 0


class CoordinatorEducationInline(admin.StackedInline):
    model = CoordinatorEducation
    extra = 0



@admin.register(CoordinatorBio)
class CoordinatorBioAdmin(admin.ModelAdmin):
    list_display = ['bio',]
    


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    inlines = [CoordinatorPhotoInline, CoordinatorProfileInline, CoordinatorBioInline, CoordinatorSkillInline, CoordinatorExperienceInline, CoordinatorBankDetailInline, CoordinatorEducationInline]
    list_display = ['id',  'team_captain', 'auth_token', 'is_verified', 'is_staff']

# 

