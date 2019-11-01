from django import forms
from .models import *
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_picture','contact'] 
        exclude=['user']  

class NeighborForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude=['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')
