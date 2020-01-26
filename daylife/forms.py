from django import forms
from django.core.exceptions import ValidationError
from .models import User


class UserForm(forms.Form):
    username = forms.CharField(max_length=32)
    email = forms.EmailField()
    pwd1 = forms.CharField(min_length=5)
    pwd2 = forms.CharField(min_length=5)

    def clean_name(self):
        name = self.cleaned_data.get('username')
        user = User.objects.filter(username=name)
        if user:
            raise ValidationError('用户名已存在不可注册')
        else:
            return name


