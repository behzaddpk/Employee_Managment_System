from django import forms
from .models import *

from django.forms import inlineformset_factory
from django.forms.widgets import SelectDateWidget
from datetime import date

class CoordinatorSkillForm(forms.ModelForm):
    
    class Meta:
        model = CoordinatorSkill
        fields = ("skill",)
        widgets = {
            'skill': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Skill'}),
        }


CoordinatorSkillFormset = inlineformset_factory(Coordinator, CoordinatorSkill, form=CoordinatorSkillForm, extra=1)



class CoordinatorExperienceForm(forms.ModelForm):
    
    class Meta:
        model = CoordinatorExperience
        fields = ("ExperiencedField", "ExperiencedYear")
        widgets = {
            'ExperiencedField': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Experienced Field'}),
            'ExperiencedYear': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Year of Experience'}),
        }

CoordinatorExperienceFormset = inlineformset_factory(Coordinator, CoordinatorExperience, form=CoordinatorExperienceForm, extra=1)

class CoordinatorEducationForm(forms.ModelForm):
    
    class Meta:
        model = CoordinatorEducation
        fields = ("StudyIn", "PassingYear")
        widgets = {
            'StudyIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Degree Name'}),
            'PassingYear': SelectDateWidget(attrs={'class': 'form-control'}),
        }

CoordinationEducationFormset = inlineformset_factory(Coordinator, CoordinatorEducation, form=CoordinatorEducationForm, extra=1)