from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput
from UserApp.models import UserProfile



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your username', }))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(
        attrs={'placeholder': 'Write Your email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your first name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Write Your last name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter New Password',
                                                    'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Repeat password',
                                                    'class': 'form-control'}),
        }



class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'first name'}),
        
        }          


CITY = [
    ('Dhaka', 'Dhaka'),
    ('Mymensign', 'Mymensign'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Barisal', 'Barisal'),
    ('Chottogram', 'Chottogram'),
    ('Khulna', 'Khulna'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']

        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'City'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        
        }