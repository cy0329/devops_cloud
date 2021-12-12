from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from mintonplace.forms import PostForm, ReviewForm
from mintonplace.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, 'mintonplace/post_list.html', {
        'post_list': qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    review_list = post.review_set.all()
    tag_list = post.tag_set.all()
    return render(request, 'mintonplace/post_detail.html', {
        'post': post,
        'review_list': review_list,
        'tag_list': tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "성공적으로 저장되었습니다.")
            return redirect('mintonplace:post_detail', saved_post.pk)
    else:
        form = PostForm()
    return render(request, 'mintonplace/post_form.html', {
        'form': form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 변경되었습니다.")
            return redirect('mintonplace:post_detail', pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mintonplace/post_form.html', {
        'form': form,
    })


def review_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.save()
            messages.success(request, "성공적으로 저장되었습니다.")
            return redirect('mintonplace:post_detail', review.pk)
    else:
        form = ReviewForm()
    return render(request, 'mintonplace/review_form.html', {
        'form': form,
    })
