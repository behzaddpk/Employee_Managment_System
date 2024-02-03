from django.contrib import admin
from .models import *


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display =['team_name']

admin.site.register(Team, TeamAdmin)


class DesignationAdmin(admin.ModelAdmin):
    list_display =['designation']

admin.site.register(Designation, DesignationAdmin)


class MemberProfileInline(admin.StackedInline):
    model = MemberProfile
    extra = 0

class MemberPhotoInline(admin.StackedInline):
    model = MemberPhoto
    extra = 0

class MemberBioInline(admin.StackedInline):
    model = MemberBio
    extra = 0


class MemberSkillInline(admin.StackedInline):
    model = MemberSkill
    extra = 0


class MemberExperienceInline(admin.StackedInline):
    model = MemberExperience
    extra = 0 


class MemberBankDetailInline(admin.StackedInline):
    model = MemberBankDetail
    extra = 0


class MemberEducationInline(admin.StackedInline):
    model = MemberEducation
    extra = 0

class MemberEvaluationInline(admin.StackedInline):
    model = MemberEvaluation
    extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    inlines = [MemberProfileInline, MemberPhotoInline, MemberEducationInline, MemberBioInline, MemberSkillInline,  MemberExperienceInline, MemberBankDetailInline, MemberEvaluationInline]
    list_display = ['team', 'auth_token', 'is_varified', 'created_at']


@admin.register(MemberEvaluation)
class MemberEvaluationAdmin(admin.ModelAdmin):
    list_display = ['member', 'Monthevaluate','Punctuality', 'Attitude', 'Performance', 'Utilities', 'Formatiing', 'Quality', 'Expertise', 'New_Learning', 'Planning', 'AI_Flowed']

    
