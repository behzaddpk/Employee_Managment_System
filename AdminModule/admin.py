from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin




class CustomUserProfileInline(admin.StackedInline):
    model = CustomUserProfile
    extra = 0



class CustomUserSkillInline(admin.StackedInline):
    model = CustomUserSkill
    extra = 0



class CustomUserExperienceInline(admin.StackedInline):
    model = CustomUserExperience
    extra = 0


class CustomUserEducationInline(admin.StackedInline):
    model = CustomUserEducation
    extra = 0


class CustomUserBioInline(admin.StackedInline):
    model = CustomUserBio
    extra = 0


class CustomUserBankDetailInline(admin.StackedInline):
    model = CustomUserBankDetail
    extra = 0





class UserModel(UserAdmin):
    inlines = [CustomUserProfileInline ,CustomUserSkillInline, CustomUserExperienceInline, CustomUserEducationInline, CustomUserBioInline, CustomUserBankDetailInline]
    list_display = ['username', 'get_designate_display','Designate']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'profile_pic', 'Designate')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, UserModel)

