from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from CYtube.models import Cyvlog


def index(request: HttpRequest) -> HttpResponse:
    qs = Cyvlog.objects.all()
    return render(
        request,
        'CYtube/index.html',
        {
            'video_list': qs,
        },
    )

def video_detail(request: HttpRequest, pk: int) -> HttpResponse:
    video = Cyvlog.objects.get(pk=pk)
    return render(
        request,
        "CYtube/video_detail.html",
        {
            "video": video,
        },
    )
