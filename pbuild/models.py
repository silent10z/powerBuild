# from django.db import models
#
#
# class User(models.Model):
#     user_number = models.AutoField(db_column='USER_NUMBER', primary_key=True, verbose_name = '사용자명')  # Field name made lowercase.
#     id = models.CharField(db_column='ID', max_length=50, verbose_name = '아이디')  # Field name made lowercase.
#     password = models.CharField(db_column='PASSWORD', max_length=50, verbose_name = '비밀번호')  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=10, verbose_name = '이름')  # Field name made lowercase.
#     email = models.CharField(db_column='EMAIL', max_length=300, verbose_name = '이메일')  # Field name made lowercase.
#     insert_day = models.DateField(db_column='INSERT_DAY', verbose_name = '가입일자', auto_now_add=True)  # Field name made lowercase.
#     coment = models.CharField(db_column='COMENT', max_length=500, blank=True, null=True, verbose_name = '하려는말')  # Field name made lowercase.
#
#     def __str__(self):
#         return self.name
#
# class Meta:
#     managed = False
#     db_table = 'user'
#
# user/models.py

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):

    user_number = models.AutoField(db_column='USER_NUMBER', primary_key=True, verbose_name='사용자명')
    email = models.EmailField('email', unique=True)
    name = models.CharField('이름', max_length=30, blank=True)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name']  # 필수입력값

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def email_user(self, subject, message, from_email=None, **kwargs):  # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)