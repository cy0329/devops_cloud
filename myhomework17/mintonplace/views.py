from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mintonplace.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, 'mintonplace/post_list.html', {
        'post_list': qs,
    })
