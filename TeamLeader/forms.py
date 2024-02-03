from django import forms
from .models import * 
from django.forms import inlineformset_factory
from django.forms.widgets import SelectDateWidget


class TeamLeaderSkillForm(forms.ModelForm):
    
    class Meta:
        model = TeamLeaderSkill
        fields = ("skill",)
        widgets = {
            'skill': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Skill'}),
        }

LeaderSkillFormset = inlineformset_factory(TeamLeader, TeamLeaderSkill, form=TeamLeaderSkillForm, extra=1)


class TeamLeaderExperienceForm(forms.ModelForm):
    
    class Meta:
        model = TeamLeaderExperience
        fields = ("ExperiencedField","ExperiencedYear")
        widgets = {
            "ExperiencedField": forms.TextInput(attrs={'class':'form-control'}),
            "ExperiencedYear": forms.TextInput(attrs={'class':'form-control'})
        }

LeaderExperiencedFormset = inlineformset_factory(TeamLeader, TeamLeaderExperience, form=TeamLeaderExperienceForm, extra=1)



class TeamLeaderEducationForm(forms.ModelForm):
    
    class Meta:
        model = TeamLeaderEducation
        fields = ("StudyIn", "PassingYear")
        widgets = {
            'StudyIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Degree Name'}),
            'PassingYear': SelectDateWidget(attrs={'class': 'form-control'}),
        }

LeaderEducationFormset = inlineformset_factory(TeamLeader, TeamLeaderEducation, form=TeamLeaderEducationForm, extra=1)