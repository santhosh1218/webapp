from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dbapp.models import Employee,Profile
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        
class Usersignupform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserupdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']





