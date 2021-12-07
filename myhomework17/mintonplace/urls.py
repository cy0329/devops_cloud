from django.urls import path
from mintonplace import views

app_name = 'mintonplace'

urlpatterns = [
    path('', views.post_list, name='post_list'),

]