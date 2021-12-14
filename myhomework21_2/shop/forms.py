from django import forms

from shop.models import Shop, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    def __init__(self, *args, **kwargs):  # '생성자' 를 만들어줄 때 __init__  언어마다 다름
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            tags = ", ".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = tags
        else:
            pass

    def save(self):
        saved_post = super().save()  # ModelForm(부모) 내의 save 기능을 호출
        # 폼에 저장된 모델의 인스턴스를 리턴 (사전형식?)
        # 인스턴스는 class의 변수
        # 기본적으로 변수에 대입한다 라고 하면 데이터 하나를 하나의 변수에 대입하는 것인데
        # 클래스의 변수는 클래스에 지정된 여러 변수들에 하나하나의 데이터를 다 대입(?)
        # 여기서 모델은 아래 class Meta를 통해 정해준 Shop
        # {'tag_set': '짜장, 짬뽕, 탕수육', 'category': '중식', 'name': 두꺼비짬뽕, ...}

        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear()
        saved_post.tag_set.add(*tag_list)
        return saved_post

    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "telephone",
            "description",
        ]


