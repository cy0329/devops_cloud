from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Post

def index(request):
    return render(request, "blog/index.html")

def post_list(request: HttpRequest)->HttpResponse:
    request.GET # QueryString Values
    request.POST # Post 요청 Values
    request.FILES # Post 요청에서 파일 Values

    qs = Post.objects.all() # QuerySet Type
    qs = qs.order_by("-pk") # -를 쓰면 내림차순 (최신 글부터 표시하기 위해)

    q = request.GET.get("q", "") # q에 아무것도 없다면 빈문자열을 가져오라는 뜻
    if q:
        qs = qs.filter(title__icontains=q) # i를 넣으면 대소문자 구별x, DB에서 썼던 like와 같은 문법

    # blog/templates/blog/post_list.html
    return render(request, "blog/post_list.html", {
        'post_list': qs,
    })

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    #pk = 1
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {
        "post": post,
    })