from django import forms
from .models import Image
from django.contrib.auth.models import User, auth

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","image")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','email']