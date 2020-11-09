from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SingUpForm
from .models import User
from django.views import generic

# index 페이지
class Index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        user_list = User.objects.all()
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
        elif not User.objects.filter(id =id).exists():
            res_data['error'] = '아이디가 존재하지 않습니다'
        else:
            puser = User.objects.get(id=id)

            if puser.password == password:
                request.session['id'] = puser.id
                request.session['user_number'] = puser.user_number
                print("새션값",request.session['id'] ,  request.session['user_number'])
                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'


        return render(request, 'main/login.html', res_data)

# 로그아웃
def logout(request):
    try:
        if request.session['id']:
            del(request.session['id'], request.session['user_number'])
        return redirect('/')
    except HttpResponseNotFound:
        raise HttpResponseNotFound("error404")

# 회원 가입

def signup(request):
    try:
        if request.method == "POST":
            form = SingUpForm(request.POST)
            print("form.is_valid():", form.is_valid())
            if form.is_valid():

                form.save()

                request.session['id'] = form.id
                return redirect("index")
            else:
                print(form.errors)
        else:
            form = SingUpForm()
        return render(request, 'insertForm/signup.html', {'form': form})
    except HttpResponseNotFound:
        raise  Http404("404 error")

# 티테일 화면으로 가기
class userDtail(generic.DetailView):
    model = User

    def get(self, request, user_number):
        print(request.session['id'], request.session['user_number'])
        user = get_object_or_404(User, pk=user_number)
        print(user)
        return render(request,"user/detail.html", {"user" : user})