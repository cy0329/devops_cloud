from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

signup = CreateView.as_view(
    form_class=UserCreationForm,
    success_url=reverse_lazy("accounts:login"),
    template_name="accounts/signup_form.html",
)

login = LoginView.as_view(
    template_name="accounts/login_form.html",
)

# TODO: 커스텀 CBV를 만든다면, LoginRequiredMixin을 상속받도록 할 수 있다.
# CBV 를 이런식으로 만들때 장식자 (@login_required)를 사용하는 방법
profile = login_required(
    TemplateView.as_view(
        template_name="accounts/profile.html",
    ))

logout = LogoutView.as_view(
    # next_page="accounts:login",
    next_page='root',
)
