from django import forms
from .models import fire_service

class EmergencyForm(forms.ModelForm):
    class Meta:
        model= fire_service
        fields='__all__'
        
            
        