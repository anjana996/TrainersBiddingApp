from django import forms
from institute.models import *
from django.forms import ModelForm
from trainers.models import *
from trainers.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class InstituteRegister(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password1","password2"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    widgets = {
        "username": forms.TextInput(attrs={'class': 'form-control'}),
        "password": forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        unam=cleaned_data.get("username")
        pwd=cleaned_data.get("password")

        if unam:
            msg="invalid username"
            self.add_error("username",msg)
class CreateJob(ModelForm):
    class Meta:
        model=JobCreation
        fields="__all__"
        widgets = {
            "job_name": forms.TextInput(attrs={'class': 'form-control'}),
        }

class JobReqForm(ModelForm):
    class Meta:
        model=JobRequirements
        fields="__all__"
        widgets = {
            "job_title": forms.Select(),
            "skills": forms.TextInput(attrs={'class': 'form-control'}),
            "qualifications": forms.TextInput(attrs={'class': 'form-control'}),
        }
class UpdateJob(ModelForm):
    class Meta:
        model=JobCreation
        fields="__all__"
        widgets = {
            "job_name": forms.TextInput(attrs={'class': 'form-control'}),}

class JobUpdateForm(ModelForm):
    class Meta:
        model=JobRequirements
        fields="__all__"
        widgets = {
            "job_title": forms.Select(),
            "skills": forms.TextInput(attrs={'class': 'form-control'}),
            "qualifications": forms.TextInput(attrs={'class': 'form-control'}),
        }
class PersonalProfileForm(ModelForm):
    class Meta:
        model=PersonalProfile
        fields="__all__"
        widgets = {
            "user": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "email": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "phonenumber": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "age": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "jobtitle": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "qualification": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "skills": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "experience": forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
            "status":forms.Select(attrs={"class":"form-control"}),

        }
class TrainerBidForm(ModelForm):
    class Meta:
        model=TrainerBidding
        fields=["user","expectedamount"]
        widgets = {
        "expectedamount":forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),}