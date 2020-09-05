from django import forms
from django.contrib.auth import get_user_model
from basic_app.models import UserProfileInfo

User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

