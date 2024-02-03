from django import forms
from .models import *
from tinymce.widgets import TinyMCE
from django.forms.widgets import SelectDateWidget

class LeaveApplicationForm(forms.ModelForm):
    
    class Meta:
        model = LeaveApplication
        fields = ( "date", "subject", "application")

        widgets = {
            'date' : SelectDateWidget(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'application': TinyMCE(attrs={'cols': 80, 'rows': 10}),
            # 'application': forms.CharField(widget=TinyMCE(attrs={'class':'form-control', 'cols': 80, 'rows': 10}))
        }