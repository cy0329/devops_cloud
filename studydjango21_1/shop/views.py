from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Category, Review


def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all()
    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__id=category_id)

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
            saved_post = form.save()
            return redirect('shop:shop_detail', saved_post.pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop/shop_form.html', {
        'form': form,
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
    return render(request, 'shop/review_form.html', {
        'form': form,
    })


