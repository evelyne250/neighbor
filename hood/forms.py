from django import forms
from .models import *
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_picture'] 
        exclude=['user','projects','contact']  

class NeighborForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','occupants']
        # exclude=['user', ]
