from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import *
from django.forms.widgets import DateInput
from django.forms.widgets import SelectDateWidget


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("team_name",)


        widgets = {
            'team_name': forms.TextInput(attrs={'class':'form-control'})
        }



class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ("designation",)
        widgets = {
            'designation': forms.TextInput(attrs={'class':'form-control'})
        }



class MemberForm(forms.ModelForm):
    DESIGNATE_CHOICES = (
        ('', 'Select One'),
        (5, 'WRITER'),
        (6, 'MEMBER'),

    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'UserName'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),  required=True) 
    team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label='Select One', to_field_name='team_name')
    designate = forms.ChoiceField(choices=DESIGNATE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}), required=True)

    class Meta:
        model = Member
        fields = ("first_name", "last_name", "username", "email",  "team", "designate", "password")

        

class MemberEvaluationForm(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=Member.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder': 'Select One'}), empty_label='Select One', to_field_name='name') 
    # Month = forms.ModelChoiceField(widget=forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Select One'}), empty_label='Select One', to_field_name='name') 
    
    # team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label='Select One', to_field_name='team_name')
    # team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label='Select One', to_field_name='team_name')
    class Meta:
        model = MemberEvaluation
        fields = (
            "member", "Monthevaluate" ,"Punctuality","Attitude", "Performance", "Utilities", "Formatiing", "Quality",
              "Expertise", "New_Learning", "Planning", "AI_Flowed"
              )

        widgets = {
            'Monthevaluate': SelectDateWidget(years=range(2000, 2051) , attrs={'class': 'form-control'}),
            'Punctuality': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5','class':'form-control', 'placeholder': 'Punctuality & Response Time + In  & Out'}),
            'Attitude': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Team Spirit + Attitude and Behavior'}),
            'Performance': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Cancellations/Quiz&exam performance'}),
            'Utilities': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Formatting & Referencing / Language Grip for IT'}),
            'Formatiing': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Content Flow & Quality / Logics and Structure'}),
            'Quality': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Understanding Instructions'}),
            'Expertise': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Expertise in Technical Subjects / Advancement in Language'}),
            'New_Learning': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Focused on New Learnings'}),
            'Planning': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Planning & Management'}),
            'AI_Flowed': forms.NumberInput(attrs={'step': '.01','min':'1','max': '5', 'class':'form-control', 'placeholder': 'Plagiarism / ChatGPT or AI Tools / Flawed Language for IT/Coursework Missed'}),
        }



class MemberSkillForm(forms.ModelForm):
    class Meta:
        model = MemberSkill
        fields = ('skill',)

        widgets = {
            'skill': forms.TextInput(attrs={'class': 'form-control'}),

        }
        

MemberSkillFormSet = inlineformset_factory(Member, MemberSkill, form=MemberSkillForm, extra=1)


class MemberExperienceForm(forms.ModelForm):
    class Meta:
        model = MemberExperience
        fields = ('ExperiencedField', 'ExperiencedYear')

        widgets = {
            'ExperiencedField': forms.TextInput(attrs={'class': 'form-control'}),
            'ExperiencedYear': forms.TextInput(attrs={'class': 'form-control'}),

        }
        

ExperienceFormSet = inlineformset_factory(Member, MemberExperience, form=MemberExperienceForm, extra=1)  



class MemberEducationForm(forms.ModelForm):


    class Meta:
        model = MemberEducation
        fields = ("StudyIn", "PassingYear")
        

        widgets = {
            'StudyIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write Experienced Field '}),
            'PassingYear': SelectDateWidget(years=range(2000, 2051), attrs={'class': 'form-control'}),



        }
        
EducationFormset = inlineformset_factory(Member, MemberEducation, form=MemberEducationForm, extra=1)