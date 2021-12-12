from django.urls import path

from mintonplace import views

app_name = 'mintonplace'
urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]

