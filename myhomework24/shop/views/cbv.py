from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review

shop_list = ListView.as_view(
    model=Shop,
)

shop_detail = DetailView.as_view(
    model=Shop,
)


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm

    def get_success_url(self):
        shop_pk = self.object.pk
        return reverse('shop:shop_detail', args=[shop_pk])


shop_new = ShopCreateView.as_view()


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm

    def get_success_url(self):
        shop_pk = self.object.pk
        return reverse('shop:shop_detail', args=[shop_pk])


shop_edit = ShopUpdateView.as_view()


class ShopDeleteView(DeleteView):
    model = Shop

    def get_success_url(self):
        return reverse('shop:shop_list')


shop_delete = ShopDeleteView.as_view()


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        shop_pk = self.object.shop.pk
        return reverse('shop:shop_detail', args=[shop_pk])


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        shop_pk = self.object.shop.pk
        return reverse('shop:shop_detail', args=[shop_pk])


review_edit = ReviewUpdateView.as_view()


class ReviewDeleteView(DeleteView):
    model = Review

    def get_success_url(self):
        shop_pk = self.object.shop.pk
        return reverse('shop:shop_detail', args=[shop_pk])


review_delete = ReviewDeleteView.as_view()

