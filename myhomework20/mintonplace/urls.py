from django.urls import path

from mintonplace import views

app_name = 'mintonplace'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_pk>/reviews/new/', views.review_new, name='review_new'),
]

