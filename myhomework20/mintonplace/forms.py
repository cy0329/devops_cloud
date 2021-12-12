from django import forms

from mintonplace.models import Post, Review


class ShopForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

