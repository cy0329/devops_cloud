from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shop.forms import ReviewForm
from shop.mixins import ReviewUserCheckMixin
from shop.models import Shop, Category, Review


class ShopListView(ListView):
    model = Shop
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["category_list"] = Category.objects.all()
        return context_data

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("query", "")
        if query:
            qs = qs.filter(name__icontains=query)
        return qs


shop_list = ShopListView.as_view()  # 클래스를 직접 호출하는건 없음 ==> 클래스.as_view로 호출

shop_detail = DetailView.as_view(
    model=Shop,
)


class ReviewCreateView(LoginRequiredMixin, CreateView):  # 다중 상속 - 지원 안하는 언어도 있지만 파이썬은 지원한다.
    model = Review
    form_class = ReviewForm

    # FIXME: shop detail 로 이동하는 것이 목표
    # success_url = reverse_lazy('shop:shop_list')  # 아래 form_valid에서 부모를 호출하지 않기 때문에, redirect(shop)으로 이미 되있어서.

    # 유효성 검사에 통과한다면 ...
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs : URL Captured 값들이 사전으로 저장
        shop_pk = self.kwargs["shop_pk"]
        shop = get_object_or_404(Shop, pk=shop_pk)

        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()
        # return redirect('shop:shop_detail', shop.pk)  # get absolute url을 써주면 좋겠지?
        return redirect(shop)


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(LoginRequiredMixin, ReviewUserCheckMixin, UpdateView):  # 다중 상속, UserPassesTestMixin 이건 아직 우리가 제대로 하기 어려움
    model = Review
    form_class = ReviewForm
    # FIXME: shop detail 로 보내기
    # success_url = reverse_lazy('shop:shop_list')

    def get_success_url(self) -> str:
        review = self.object
        return resolve_url(review.shop)   # 리턴값이 다르기 때문에, str 로 리턴이면 resolve_url, HttpResponse 로 리턴이면 reverse


review_edit = ReviewUpdateView.as_view()
