from django.contrib import messages
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from diary.forms import PostForm, CommentForm
from diary.models import Post, Comment


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
    post = get_object_or_404(Post, pk=pk)
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404  # 예외 발생

    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()
    return render(request, 'diary/post_detail.html', {
        'post': post,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data
            post = form.save(commit=False)
            post.ip = request.META["REMOTE_ADDR"]
            post.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect('diary:post_list')
    else:
        form = PostForm()

    return render(request, "diary/post_form.html", {
        "form": form,
    })


# 수정도 detail처럼 수정대상을 지정하기 위해 pk를 인자로 받아줘야함
def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    # 아래 코드는 ModelForm에 한해서 동작하는 코드
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        # ModelForm이기에 instance 넣는게 가능
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect('diary:post_list')
    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })
    # pass라고 쓰는것이나 return None이나 같음 -> Response가 없다는 오류 뜸


# /diary/100/comments/new/
def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data  # 유효성 검사에 통과한 값들 (dict)
            comment = form.save(commit=False)
            # comment.post_id = post_pk # FK를 직접 채우진 않는다.
            comment.post = post
            comment.save()
            return redirect("diary:post_detail", post_pk)
    else:
        form = CommentForm()
    return render(request, 'diary/comment_form.html', {
        "form": form,
    })


# /diary/100/comments/20/edit
def comment_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)  # 수정 대상을 지정한 것 (인스턴스를 사용해)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect('diary:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'diary/comment_form.html', {
        'form': form,
    })
