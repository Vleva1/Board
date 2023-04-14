from django import forms
from django.contrib.auth.forms import UserCreationForm
from board.models import Authors



class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль')

    class Meta:
        fields = ['username', 'password']


class SignatureForm(forms.Form):
    signature = forms.CharField(label='Код')

    class Meta:
        fields = ['signature']


# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Enter name'
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Enter last_name'
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Enter username'
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Enter email'
#     }))
#     password_1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Enter password'
#     }))
#     password_2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Repeat password'
#     }))
#
#     class Meta:
#         model = Authors
#         fields = ('first_name', 'last_name', 'username', 'email', 'password_1', 'password_2')
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=True)
#         return user






