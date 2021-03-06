from django.urls import path
from . import views



urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('blog/single/', views.BlogSingle.as_view(), name='blog-single'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('features/', views.Feature.as_view(), name='features'),
    path('pricing/', views.Pricing.as_view(), name='pricing'),
    # path('join/', views.UserCreateView.as_view(), name="join"),
    path('login/', views.login, name="login"),
    # 디테일 뷰로가면 유저 번호를 보내준다
    path('detail/<int:user_number>', views.userDtail.as_view(), name="detail"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup")
]