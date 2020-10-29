from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('', views.Index.as_view(), name='blog'),
    path('', views.Index.as_view(), name='blog-single'),
    path('', views.Index.as_view(), name='contact'),
    path('', views.Index.as_view(), name='fearures'),
    path('', views.Index.as_view(), name='pricing'),
]