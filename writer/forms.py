from django import forms
from .models import *
from django.forms import inlineformset_factory
from django.forms.widgets import SelectDateWidget



class WriterSkillForm(forms.ModelForm):
    
    class Meta:
        model = WriterSkill
        fields = ("skill",)
        widgets = {
            'skill': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Skill'}),
        }

WriterSkillFormset = inlineformset_factory(Writer, WriterSkill, form=WriterSkillForm, extra=1)


class WriterExperienceForm(forms.ModelForm):
    
    class Meta:
        model = WriterExperience
        fields = ("ExperiencedField", "ExperiencedYear")
        widgets = {
            'ExperiencedField' :  forms.TextInput(attrs={'class':'form-control', 'placeholder':'Writer Experience in Field'}),
            'ExperiencedYear': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Writer Experience in Field'})
        }

WriterExperienceFormset = inlineformset_factory(Writer, WriterExperience, form=WriterExperienceForm, extra=1)


class WriterEducationForm(forms.ModelForm):
    
    class Meta:
        model = WriterEducation
        fields = ("StudyIn", "PassingYear")
        widgets = {
            'StudyIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Degree Name'}),
            'PassingYear': SelectDateWidget(attrs={'class': 'form-control'}),
        }

WriterEducationFormset = inlineformset_factory(Writer, WriterEducation, form=WriterEducationForm, extra=1)