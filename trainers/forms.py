from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from trainers.models import PersonalProfile,TrainerBidding
class TrainerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        # widgets = {
        #     "first_name": forms.TextInput(attrs={'class': 'form-control'}),
        #     "last_name": forms.TextInput(attrs={'class': 'form-control'}),
        #     "email": forms.TextInput(attrs={'class': 'form-control'}),
        #     "username": forms.TextInput(attrs={'class': 'form-control'}),
        #     "password1": forms.TextInput(attrs={'class': 'form-control'}),
        #     "password2": forms.TextInput(attrs={'class': 'form-control'}),
        # }

class TrianerLoginForm():
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    widgets = {
        "username": forms.TextInput(attrs={'class': 'form-control'}),
        "password": forms.TextInput(attrs={'class': 'form-control'})
    }
    def clean(self):
        print("c")
class PersonalProfileForm(ModelForm):
    class Meta:
        model=PersonalProfile
        fields="__all__"
        widgets = {
            "user": forms.TextInput(attrs={'class': 'form-control'}),
            "phonenumber": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.TextInput(attrs={'class': 'form-control'}),
            "jobtitle": forms.Select(),
            "qualification": forms.TextInput(attrs={'class': 'form-control'}),
            "skills": forms.TextInput(attrs={'class': 'form-control'}),
            "experience": forms.TextInput(attrs={'class': 'form-control'}),
            "status":forms.HiddenInput()

        }


    def clean(self):
        cleaned_data = super().clean()
        users = cleaned_data.get('user')
        ages = cleaned_data.get('age')
        experiences=cleaned_data.get('experience')

        uname = PersonalProfile.objects.filter(user=users)

        if ages>35:
            msg = "Please enter a valid age"
            self.add_error('age', msg)
        if experiences>10:
            msg="please enter a valid experience from 0-10"
            self.add_error("experience",msg)
class TrainerBidForm(ModelForm):
    class Meta:
        model=TrainerBidding
        fields=["user","expectedamount"]
        widgets = {
            "user":forms.TextInput(attrs={'class': 'form-control'}),

        "expectedamount":forms.TextInput(attrs={'class': 'form-control'}),}

    def clean(self):
        cleaned_data = super().clean()
        users = cleaned_data.get('user')
        amount=cleaned_data.get('expectedamount')
        valid=TrainerBidding.objects.filter(user=users)

        if amount>5000:
            msg="We are sorry! Please enter a valid amount"
            self.add_error('expectedamount',msg)

class PersonalProfileEditForm(ModelForm):
    class Meta:
        model=PersonalProfile
        fields="__all__"
        widgets = {
            "user": forms.TextInput(attrs={'class': 'form-control'}),
            "emailId": forms.TextInput(attrs={'class': 'form-control'}),
            "phonenumber": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.TextInput(attrs={'class': 'form-control'}),
            "jobtitle": forms.Select(),
            "qualification": forms.TextInput(attrs={'class': 'form-control'}),
            "skills": forms.TextInput(attrs={'class': 'form-control'}),
            "experience": forms.TextInput(attrs={'class': 'form-control'}),
            "status":forms.HiddenInput()

        }

    def clean(self):
        cleaned_data = super().clean()
        users = cleaned_data.get('user')
        ages = cleaned_data.get('age')
        experiences=cleaned_data.get('experience')

        uname = PersonalProfile.objects.filter(user=users)

        if ages>35:
            msg = "Please enter a valid age"
            self.add_error('age', msg)
        if experiences>10:
            msg="please enter a valid experience from 0-10"
            self.add_error("experience",msg)