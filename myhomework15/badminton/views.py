from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from badminton.forms import MintonForm
from badminton.models import Minton

# CBV 방식으로 해보기
# list = ListView.as_view(model=Minton, template_name="badminton/minton_list.html")


def minton_list(request: HttpRequest) -> HttpResponse:
    qs = Minton.objects.all()
    query = request.GET.get("query", "")

    if query:
        qs = qs.filter(name__icontains=query)

    template_name = 'badminton/minton_list.html'
    context_data = {
        'minton_list': qs,
    }
    return render(request, template_name, context_data)

def minton_detail(request: HttpRequest, pk: int) -> HttpResponse:
    minton = Minton.objects.get(pk=pk)
    template_name = 'badminton/minton_detail.html'
    context_data = {
        'minton': minton,
    }
    return render(request, template_name, context_data)


def minton_new_1(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "badminton/minton_form_1.html", {})
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        address = request.POST["address"]
        telephone = request.POST["telephone"]
        # 유효성 검사 필요
        Minton.objects.create(
            name=name,
            description=description,
            address=address,
            telephone=telephone,
        )
        return redirect("/badminton/")

minton_new = CreateView.as_view(
    model=Minton,
    form_class=MintonForm,
    success_url="/badminton/",
)

