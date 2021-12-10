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
## 폼 필드를 직접 지정해줄때는 위의 방식

from diary.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        # 장고가 알아서 Post 모델에 있는 필드들을 다 복사해서 가져와 줌

        # 유저로부터 입력받을 필드 이름을 나열
        fields = [
            "author_name",
            "title",
            "content",
            "photo",
            "tag_set",
        ]
        # 이 필드에 대해서만 html을 보여주고, 유효성 검사를 하고, db에 저장함


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "message"]
