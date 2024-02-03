from django.contrib import admin
from django import forms
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.


class PartnerBioForm(forms.ModelForm):
    bio = forms.CharField(widget=TinyMCE())

    class Meta:
        model = PartnerBio
        fields = '__all__'

class PartnerBioInline(admin.StackedInline):
    model = PartnerBio
    form = PartnerBioForm
    extra = 0

class PartnerPhotoInline(admin.StackedInline):
    model = PartnerPhoto
    extra = 0


class PartnerProfileInline(admin.StackedInline):
    model = PartnerProfile
    extra = 0

# class PartnerBioInline(admin.StackedInline):
#     model = PartnerBio
#     list_display = ['bio']
#     extra = 0

class PartnerSkillInline(admin.StackedInline):
    model = PartnerSkill
    extra = 0

class PartnerExperienceInline(admin.StackedInline):
    model = PartnerExperience
    extra = 0

class BankDetailInline(admin.StackedInline):
    model = BankDetail
    extra = 0


class PartnerEducationInline(admin.StackedInline):
    model = PartnerEducation
    extra = 0



@admin.register(PartnerBio)
class PartnerBioAdmin(admin.ModelAdmin):
    list_display = ['bio',]
    


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    inlines = [PartnerPhotoInline, PartnerProfileInline, PartnerBioInline, PartnerSkillInline, PartnerExperienceInline, BankDetailInline, PartnerEducationInline]
    list_display = ['id',  'team_captain', 'auth_token', 'is_verified', 'is_staff']



