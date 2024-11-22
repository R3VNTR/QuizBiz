from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'profile_picture']

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')

        if profile_picture:
            if profile_picture.size > 5 * 1024 * 1024:
                raise ValidationError(
                    "Profile picture size cannot exceed 5MB.")

        return profile_picture


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture']
