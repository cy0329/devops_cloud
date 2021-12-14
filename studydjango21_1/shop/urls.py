from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('new/', views.shop_new, name='shop_new'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),
    path('<int:pk>/edit/', views.shop_edit, name='shop_edit'),
    path('<int:shop_pk>/reviews/new/', views.review_new, name='review_new'),
    path('<int:shop_pk>/reviews/<int:review_pk>/edit/', views.review_edit, name='review_edit'),
]

