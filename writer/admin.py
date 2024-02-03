from django.contrib import admin
from django import forms
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.


class WriterBioForm(forms.ModelForm):
    bio = forms.CharField(widget=TinyMCE())

    class Meta:
        model = WriterBio
        fields = '__all__'

class WriterBioInline(admin.StackedInline):
    model = WriterBio
    form = WriterBioForm
    extra = 0

class WriterPhotoInline(admin.StackedInline):
    model = WriterPhoto
    extra = 0


class WriterProfileInline(admin.StackedInline):
    model = WriterProfile
    extra = 0

# class WriterBioInline(admin.StackedInline):
#     model = WriterBio
#     list_display = ['bio']
#     extra = 0

class WriterSkillInline(admin.StackedInline):
    model = WriterSkill
    extra = 0

class WriterExperienceInline(admin.StackedInline):
    model = WriterExperience
    extra = 0

class BankDetailInline(admin.StackedInline):
    model = BankDetail
    extra = 0


class WriterEducationInline(admin.StackedInline):
    model = WriterEducation
    extra = 0



@admin.register(WriterBio)
class WriterBioAdmin(admin.ModelAdmin):
    list_display = ['bio',]
    


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    inlines = [WriterPhotoInline, WriterProfileInline, WriterBioInline, WriterSkillInline, WriterExperienceInline, BankDetailInline, WriterEducationInline]
    list_display = ['id',  'team', 'auth_token', 'is_verified', 'is_staff']



