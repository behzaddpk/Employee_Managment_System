from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    
        class Meta:
            model = Client
            fields = ("Full_name", "email", "country", 'country', 'contactno', 'bank_account', 'weblink', 'img')

            widgets = {
                'Full_name': forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
                'country': forms.TextInput(attrs={'class':'form-control'}),
                'contactno': forms.TextInput(attrs={'class':'form-control'}),                      
                'bank_account': forms.TextInput(attrs={'class':'form-control'}),                      
                'weblink': forms.TextInput(attrs={'class':'form-control'}),                      
                'img': forms.FileInput(attrs={'class':'form-control', 'accept':'image/*'}),                      
            }

