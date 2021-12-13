from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from shop.forms import ShopForm
from shop.models import Shop, Category, Tag


def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
        'category_list': category_qs,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()

            return redirect('shop:shop_detail', saved_post.pk)
    else:
        form = ShopForm()
    return render(request, 'shop/shop_form.html', {
        'form': form,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_post = form.save()
            return redirect('shop:shop_detail', saved_post.pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, 'shop/shop_form.html', {
        'form': form,
    })

