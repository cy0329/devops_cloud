from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from badminton.models import Minton


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'badminton/index.html')

def minton_list(request: HttpRequest) -> HttpResponse:
    qs = Minton.objects.all()
    template_name = 'badminton/minton_list.html'
    context_data = {
        "minton_list": qs,
    }
    return render(request, template_name, context_data)

def minton_detail(request: HttpRequest, pk: int) -> HttpResponse:
    minton = Minton.objects.get(pk=pk)
    template_name = 'badminton/minton_detail.html'
    context_data = {
        "minton": minton,
    }
    return render(request, template_name, context_data)