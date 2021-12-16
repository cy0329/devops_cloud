from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ShopForm
from shop.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:shop_list')
    else:
        form = ShopForm()
    return render(request, 'shop/shop_form.html', {
        'form': form,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_shop = form.save()
            return redirect('shop:shop_detail', saved_shop.pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop/shop_form.html', {
        'form': form,
    })


def shop_delete(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        shop.delete()
        return redirect('shop:shop_list')
    return render(request, 'shop/shop_confirm_delete.html', {
        'shop': shop,
    })