from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import User
# Create your views here.

# 함수 형식

# 제내릭 뷰 형식

from django.views import generic

# index 페이지
class Index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        user_list = User.objects.all()
        print(user_list)
        return render(request, template_name, {"user_list": user_list})

# blog 페이지
class Blog(generic.TemplateView):
    def get(self, request):
        template_name = "main/blog.html"
        return render(request, template_name)
# blog 싱글 페이지
class BlogSingle(generic.TemplateView):
    def get(self, request):
        template_name = "main/blog-single.html"
        return render(request, template_name)

# feature page
class Feature(generic.TemplateView):
    def get(self,request):
        temptlate_name = 'main/features.html'
        return render(request, temptlate_name)

# contact page
class Contact(generic.TemplateView):
    def get(self,request):
        template_name = 'main/contact.html'
        return render(request, template_name)

class Pricing(generic.TemplateView):
    def get(self,request):
        template_name = 'main/pricing.html'
        return render(request, template_name)

# 회원가입 폼
from .forms import UserForm
class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'insertForm/signup.html'
    success_url = "/"

# 로그인 뷰로 가기
class LoginView(generic.TemplateView):
    def get(self,request):
        template_name = 'main/login.html'
        return render(request, template_name)