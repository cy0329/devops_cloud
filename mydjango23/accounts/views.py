from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from PIL import Image


def profile_image(request: HttpRequest) -> HttpResponse:
    canvas = Image.new("RGBA", (256, 256), (255, 0, 255, 255))
    # text/image
    response = HttpResponse(content_type="image/png")
    canvas.save(response, "PNG")
    return response


# def login(request):
#     pass

login = LoginView.as_view(
    template_name='accounts/login_form.html',
)


# 새로운 User 인스턴스를 만드는 것.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


# 위 == 아래
# signup = CreateView.as_view(
#     form_class=UserCreationForm,
#     success_url=reverse_lazy("accounts:login"),
#     template_name="accounts/signup_form.html",
# )

@login_required  # 로그인이 필요한 url로 자동 연결  (주소 뒤에 ?next=urlreverse가 붙음)
def profile(request):
    return render(request, 'accounts/profile.html')


logout = LogoutView.as_view(
    next_page='accounts:login',
)
# 이런거 구현할때 컨트롤 클릭으로 LogoutView 클릭해서 안에 지원하는게 뭐가 있는지 보고 괄호 안에서
# 변경해줘서 구현할 수 있음
