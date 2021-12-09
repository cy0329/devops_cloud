from django import forms
from django.core.validators import RegexValidator


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    phone = forms.CharField(
        validators=[
            RegexValidator(r"^\d{3}-?\d{3,4}-?\d{4}$", message="전화번호를 입력해주세요."),
        ],
    )
