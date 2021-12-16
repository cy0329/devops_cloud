from django import forms

from blog.models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField()

    # 초기값 지정 ( 생성자 함수 사용 )
    def __init__(self, *args, **kwargs):  # 팩킹
        super().__init__(*args, **kwargs)  # 언팩킹

        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            initial = ", ".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = initial

    # DB로의 저장
    # def save(self, commit=True):
    #     saved_post = super().save(commit)
    #     # ...
    #     return saved_post
    # 아래 함수가 호출되기 전에, instance.save()가 호출 되었음을 보장받는다.
    def _save_m2m(self):  # m2m은 리턴받을 것도 없음, 함수만 처리해주면 됨
        super()._save_m2m()

        tag_list = []
        tags = self.cleaned_data.get("tag","")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        self.instance.tag_set.clear()
        self.instance.tag_set.add(*tag_list)

    class Meta:
        model = Post
        fields = [
            "category",
            "title",
            "content",
            "photo",
            "status",
        ]
