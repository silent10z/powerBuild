from django.shortcuts import render, redirect

# Create your views here.

# 함수 형식
def index(request):
    return render(request, 'main/index.html')

# 제내릭 뷰 형식

from django.views import generic

class Index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        return render(request, template_name)