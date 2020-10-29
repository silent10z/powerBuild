from django.shortcuts import render, redirect
from .models import User
# Create your views here.

# 함수 형식

# 제내릭 뷰 형식

from django.views import generic

class Index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        user_list = User.objects.all()
        print(user_list)
        return render(request, template_name, {"user_list": user_list})