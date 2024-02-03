from django.contrib import admin
from .models import TaskCategory, InstitutionName, AssessmentType, TaskDetail

# Register your models here.


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ['taskname']


@admin.register(InstitutionName)
class InstitutionNameAdmin(admin.ModelAdmin):
    list_display = ['InstitutionName']


@admin.register(AssessmentType)
class AssessmentTypeAdmin(admin.ModelAdmin):
    list_display = ['AssessmentName']


@admin.register(TaskDetail)
class TaskDetailAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'client',  'task_category', 'institution_name', 'course_code', 'deadline', 'instruction', 'word_count', 'assessment_type', 'attachment_file', 'send_to', 'task_status']
