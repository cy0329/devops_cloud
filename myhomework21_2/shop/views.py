from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from shop.forms import ShopForm, ReviewForm
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
    review_list = shop.review_set.all()
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
        'review_list': review_list,
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


def review_new(request: HttpRequest, shop_pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=shop_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        form.save()
        return redirect('shop:shop_detail', shop.pk)
    else:
        form = ReviewForm()

    return render(request, 'shop/review_form.html', {
        'form': form,
    })