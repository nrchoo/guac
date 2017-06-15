from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from guac_manage.models import Company,Package

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'size': '40'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'size': '40'}), label = 'First Name')
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'size': '40'}), label = 'Last Name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'size': '40'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'size': '40'}), label = 'Password')
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'size': '40'}), label = 'Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CompanyForm(ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'size': '40'}), label = 'Company Name')
    address = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'size': '40'}), label = 'Address')
    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'size': '40'}), label = 'Phone #')
    class Meta:
        model = Company
        fields = ['name','address','phone']


class PackageForm(ModelForm):

    package_choices = (
        ("BEGINNER", 'Beginner'),
        ("INTERMEDIATE", 'Intermediate'),
        ("PROFESSIONAL", 'Professional'),
    )

    package_type = forms.ChoiceField(choices=package_choices, widget=forms.RadioSelect())


    class Meta:
        model = Package
        fields = ['package_type']
