from django import forms
from .models import *
from team.models import Team


class CustomUserForm(forms.ModelForm):
    DESIGNATE_CHOICES = (
        ('', 'Select One'),
        (1, 'ADMIN'),
        (2, 'PARTNER'),
        (3, 'COORDINATOR'),
        (4, 'TEAM LEADER'),

    )


    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'UserName'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),  required=True) 
    team_captain = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label='Select One', to_field_name='team_name')
    designate = forms.ChoiceField(choices=DESIGNATE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}), required=True)


    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','username', 'email',  "team_captain", "designate", 'password')



