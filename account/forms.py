from django.contrib.auth.models import User
from django import forms
from .models import Themes, Post

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class ThemeCreateForm(forms.ModelForm):
    name = forms.CharField(label = 'Название темы', widget = forms.TextInput)
    forum_id = 1
    start_msg_usr_id = 1
    class Meta:
        model = Themes
        fields = ('name', 'id')

class PostCreateForm(forms.ModelForm):
    msg_text = forms.TextInput()
    class Meta:
        model = Post
        fields = ('msg_text', 'id')