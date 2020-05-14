from django import forms
from . import models


class LoginForm(forms.Form):

    """ LoginForm Definition """

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(
        self,
    ):  # 이메일이나 비밀번호가 있는 field를 확인하고 싶다면 clean_ 으로 시작하는 method를 써야한다!
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        return "abc"
