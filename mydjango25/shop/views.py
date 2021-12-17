from django.views.generic import ListView, DetailView

from shop.models import Shop, Category


class ShopListView(ListView):
    model = Shop

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["category_list"] = Category.objects.all()
        return context_data


shop_list = ShopListView.as_view()  # 클래스를 직접 호출하는건 없음 ==> 클래스.as_view로 호출


shop_detail = DetailView.as_view(
    model=Shop,
)