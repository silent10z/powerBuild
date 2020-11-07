from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages
from .forms import SingUpForm

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
        template_name = 'main/detail.html'
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
# class LoginView(generic.TemplateView):
#     def get(self,request):
#         template_name = 'main/login.html'
#         return render(request, template_name)

# 로그인 하기
# class UserLoginView(LoginView):
#     template_name = 'user/login.html'
#     success_url = "/"
#     def from_invalid(self, form):
#         messages.error(self.request, '로그인에 실패하였습니다', extra_tags='danger')

# 로그인 기능
# def login(request):
#     template_name = 'main/index.html'
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username='john', password='secret')
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
# 로그인
def login(request):
    # error 메세지 담을 변수
    res_data = {}
    # get 방식으로 요청이 올 떄
    if request.method == "GET":
        # login page로 보내줌
        return render(request, 'main/login.html')
    # post 방식으로 요청이 올때
    elif request.method == "POST":
        # 폼에서 전달받은 post 값 들 정의하기
        id = request.POST.get('id')
        password = request.POST.get('password')

        if not (id and password):
            res_data['error'] = '아이디와 비밀번호 모두 입력해주세요'
        else:
            try:
                puser = User.objects.get(id=id)
                if puser.password == password:
                    request.session['user'] = puser.id

                    return redirect('/')
                else:
                    res_data['error'] = '비밀번호가 틀렸습니다.'
            except:
                    res_data['error'] = '아이디가 존재하지 않습니다'
        return render(request, 'main/login.html', res_data)

# 로그아웃
def logout(request):
    if request.session['user']:
        del(request.session['user'])
    return redirect('/')

# 회원 가입

def signup(request):
    if request.method == "GET":
        form = SingUpForm()
        return render(request, 'insertForm/signup.html', {'form': form })
    elif request.method == "POST":
        form = SingUpForm(request.POST)

        if form.is_valid():
            form.save()
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            puser = User.objects.get(id=id)
            print(puser)
            if puser is not None and puser.password == password:
                request.session['user'] = puser.id

                return redirect('/')

        return render(request, 'main/login.html')



class userDtail(generic.TemplateView):
    def get(self, request):

        return render(request,"user/detail.html")