from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . models import UserProfile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm (forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'phone_number']


class UserProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'phone_number', 'profile_picture']
