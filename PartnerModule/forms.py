from django import forms
from team.models import Team
from .models import *
from AdminModule.models import *
from django.forms import inlineformset_factory
from tinymce.widgets import TinyMCE
from django.forms.widgets import SelectDateWidget



class PartnerPhotoForm(forms.ModelForm):
    
    class Meta:
        model = PartnerPhoto
        fields = ("img",)

        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control'})
        }


class PartnerProfileForm(forms.ModelForm):
    
    class Meta:
        model = PartnerProfile
        fields = ("contact_no", "address")

ProfileFormSet=inlineformset_factory(Partner, PartnerProfile, form= PartnerProfileForm, extra=0)



class PartnerSkillForm(forms.ModelForm):
    
    class Meta:
        model = PartnerSkill
        fields = ("skill",)
        widgets = {
            'skill': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Skill'}),
        }

PartnerSkillFormSet = inlineformset_factory(Partner, PartnerSkill, form=PartnerSkillForm, extra=1)


class PartnerExperienceForm(forms.ModelForm):
    
    class Meta:
        model = PartnerExperience
        fields = ("ExperiencedField", "ExperiencedYear")

        widgets = {
            'ExperiencedField': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Experienced Field '}),
            'ExperiencedYear': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Write Experienced Year '}),

        }

PartnerExperienceFormset = inlineformset_factory(Partner, PartnerExperience, form=PartnerExperienceForm, extra=1)



class PartnerBioForm(forms.ModelForm):
    bio = forms.CharField(widget=TinyMCE(attrs={'class':'form-control', 'cols': 80, 'rows': 10}))
    class Meta:
        model = PartnerBio
        fields = ("bio",)
        

        
PartnerBioFormset = inlineformset_factory(Partner, PartnerBio, form=PartnerBioForm, extra=1)


class PartnerEducationForm(forms.ModelForm):


    class Meta:
        model = PartnerEducation
        fields = ("StudyIn", "PassingYear")
        

        widgets = {
            'StudyIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Experienced Field '}),
            'PassingYear': SelectDateWidget(attrs={'class': 'form-control'}),

        }
        
PartnerEducationFormset = inlineformset_factory(Partner, PartnerEducation, form=PartnerEducationForm, extra=1)