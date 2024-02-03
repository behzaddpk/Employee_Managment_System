from django import forms
from clients.models import Client
from .models import TaskCategory, InstitutionName, AssessmentType, TaskDetail
from team.models import Member
# from bootstrap_datepicker_plus import DatePickerInput
from tinymce.widgets import TinyMCE
import calendar
from AdminModule.models import *
from django.forms.widgets import SelectDateWidget

class TaskCategoryForm(forms.ModelForm):
    
    class Meta:
        model = TaskCategory
        fields = ("taskname",)
        widgets = {
            'taskname' : forms.TextInput(attrs={'class': 'form-control'})
        }



class InstitutionNameForm(forms.ModelForm):
    
    class Meta:
        model = InstitutionName
        fields = ("InstitutionName",)
        widgets = {
            'InstitutionName' : forms.TextInput(attrs={'class': 'form-control'})
        }

class AssessmentTypeForm(forms.ModelForm):
    
    class Meta:
        model = AssessmentType
        fields = ("AssessmentName",)
        widgets = {
            'AssessmentName' : forms.TextInput(attrs={'class': 'form-control'})
        }

class TaskDetailForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder': 'Select One'}), empty_label='Select One')
    task_category = forms.ModelChoiceField(queryset=TaskCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label='Select One')
    institution_name = forms.ModelChoiceField(queryset=InstitutionName.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label='Select One')
    assessment_type = forms.ModelChoiceField(queryset=AssessmentType.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label='Select One')
    send_to = forms.ModelChoiceField(queryset=Member.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label='Select One')


    class Meta:
        model = TaskDetail
        fields = ("task_name", "client", "task_category", "institution_name", "course_code", "deadline", "instruction","word_count", "assessment_type", "attachment_file", "send_to")

        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': SelectDateWidget(attrs={'class': 'form-control'}),
            'instruction': forms.TextInput(attrs={'class': 'form-control'}),
            'word_count': forms.TextInput(attrs={'class': 'form-control'}),
            'attachment_file': forms.FileInput(attrs={'class': 'form-control'}),
            'send_to': forms.TextInput(attrs={'class': 'form-control'}),
        }
