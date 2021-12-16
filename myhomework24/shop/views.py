from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review


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
    review_list = shop.review_set.all()
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
        'review_list': review_list,
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


def review_new(request: HttpRequest, shop_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.save()
            return redirect('shop:shop_detail', shop_pk)
    else:
        form = ReviewForm()
    return render(request, 'shop/review_form.html', {
        'form': form,
    })


def review_edit(request: HttpRequest, shop_pk: int, review_pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('shop:shop_detail', shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'shop/shop_form.html', {
        "form": form,
    })


def review_delete(request: HttpRequest, shop_pk: int, review_pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        review.delete()
        return redirect('shop:shop_detail', shop_pk)
    return render(request, 'shop/review_confirm_delete.html', {
        'review': review,
    })
