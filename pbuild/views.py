from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages

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
        messages.add_message(request, messages.INFO, 'Hello world.')
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
# from .forms import UserForm
# class UserCreateView(CreateView):
#     form_class = UserForm
#     template_name = 'insertForm/signup.html'
#     success_url = "/"
#
#     def post(self, request):
#         super(UserCreateView, self).post(request)
#         id = request.POST['id']
#         password = request.POST['password']
#         print("아이디와 페스워드", [id, password])
#         messages2 = {"회원가입 완료"}
#         template_name = 'main/index.html'
#         res_data = {}
#         res_data['meassage2'] = "회원가입 완료"
#         return render(request, template_name, res_data)
# 로그인 뷰로 가기
class LoginView(generic.TemplateView):
    def get(self,request):
        template_name = 'main/login.html'
        return render(request, template_name)

# 로그인 하기
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = "/"
    def from_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다', extra_tags='danger')

# # 로그인 기능
# def login(request):
#     template_name = 'main/login.html'
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#         username = request.POST.get('name')
#         password = request.POST.get('password')
#
#         res_data = {}
#         if not (username and password):
#             res_data['error'] = "모든 칸을 다 입력해주세요"
#         else:
#             fuser = User.objects.get(name = username)
#
#         if check_password(password, fuser.password):
#             request.session['user']= fuser.id
#
#             return redirect('/')
#         else:
#             res_data['error'] = "비밀번호가 틀렸습니다."
#     return render(request, template_name, res_data)
