from django.db.models import query
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from badminton.models import Minton

mlist = ListView.as_view(model=Minton, template_name='badminton/minton_list.html')


# def minton_list(request: HttpRequest) -> HttpResponse:
#     qs = Minton.objects.all()
#     query = request.GET.get("query", "")
#     if query:
#         qs = qs.filter(name__icontains=query)
#
#     template_name = 'badminton/minton_list.html'
#     context_data = {
#         'minton_list': qs,
#     }
#     return render(request, template_name, context_data)

mdetail = DetailView.as_view(model=Minton, template_name='badminton/minton_detail.html')

# def minton_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     minton = Minton.objects.get(pk=pk)
#     template_name = 'badminton/minton_detail.html'
#     context_data = {
#         'minton': minton,
#     }
#     return render(request, template_name, context_data)

