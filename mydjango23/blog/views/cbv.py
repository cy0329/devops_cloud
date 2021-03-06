# Class Based View(CBV)
#  - 뷰 함수를 만들어주는 클래스
from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post

post_list = ListView.as_view(
    model=Post,
)

post_detail = DetailView.as_view(
    model=Post,
)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    # success_url = reverse_lazy('blog:post_list')

    # def get_success_url(self):  # class 안의 함수로 지정해줌으로서 가변적인 상황을 만들 수 있음
    #     # self.object  # 저장된 모델 인스턴스 -> Post 모델의 인스턴스
    #     post_pk = self.object.pk
    #     return reverse('blog:post_detail',
    #                    args=[post_pk])  # 리턴값 : 문자열 # 얘만 args 로 써줌, 가장 기본이 되는 함수 reverse -> 이게 베이스로 아래 두가지 함수가 다 사용
        # return resolve_url('blog:post_detail', post_pk)       # 리턴값 : 문자열  # 얘가 기능이 더 많음
        # return redirect   ('blog:post_detail', post_pk)       # 리턴값 : HttpResponse
        #       {% url "blog:post_detail" post_pk %}            # 문자열


post_new = PostCreateView.as_view()


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    # def get_success_url(self):  # class 안의 함수로 지정해줌으로서 가변적인 상황을 만들 수 있음
    #     # self.object  # 저장된 모델 인스턴스 -> Post 모델의 인스턴스
    #     post_pk = self.object.pk
    #     return reverse('blog:post_detail', args=[post_pk])


post_edit = PostUpdateView.as_view(
    # model=Post,
    # form_class=PostForm,
    # TODO: 가변적으로 URL을 지정할 수 없다. (현 시점에서는)
    # TODO: URL Reverse가 미적용
    # success_url='/blog/',
    # success_url="blog:post_list",   # URL Reverse 미지원
    # success_url=reverse('blog:post_list'),  # 함수 호출 시점에 바로 사용
    # success_url=reverse_lazy('blog:post_list'),  # 함수 호출 시점에 바로 사용되지 않고 필요할 때까지 대기
)

post_delete = DeleteView.as_view(
    model=Post,
    success_url=reverse_lazy('blog:post_list'),
)
