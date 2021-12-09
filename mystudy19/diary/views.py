from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from diary.forms import PostForm
from diary.models import Post


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "diary/tag_detail.html", {
        "tag_name": tag_name,
        "post_list": qs,
    })


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    # 여기부터
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)
    # 여기까지 검색기능
    return render(request, "diary/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()
    return render(request, 'diary/post_detail.html', {
        'post': post,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    form = PostForm()
    return render(request, 'diary/post_form.html', {
        'form': form,
    })
