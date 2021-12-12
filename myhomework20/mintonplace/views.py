from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from mintonplace.forms import PostForm
from mintonplace.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    pass


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Post, pk=pk)
    review_list = shop.review_set.all()
    tag_list = shop.tag_set.all()
    return render(request, 'post/post_detail.html', {
        'shop': shop,
        'review_list': review_list,
        'tag_list': tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("구현 예정")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "성공적으로 저장되었습니다.")
            return redirect('shop:shop_detail', saved_post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {
        'form': form,
    })

