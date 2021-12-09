from django import forms
from django.core.validators import RegexValidator

# class PostForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()
#     phone = forms.CharField(
#         validators=[
#             RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$", message="휴대폰 번호를 입력해주세요."),
#         ]
#     )
from diary.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
    # 장고가 알아서 Post 모델에 있는 필드들을 다 복사해서 가져와 줌

