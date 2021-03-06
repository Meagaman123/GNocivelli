from django import forms
from django.contrib.auth.models import User
from reviewproduct.models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['name', 'dateofbirth', 'address', 'town', 'country', 'profile_picture']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country','town','address','dateofbirth','name', 'profile_picture']
        