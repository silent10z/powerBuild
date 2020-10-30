from django.db import models


class User(models.Model):
    user_number = models.AutoField(db_column='USER_NUMBER', primary_key=True, verbose_name = '사용자명')  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=50, verbose_name = '아이디')  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, verbose_name = '비밀번호')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10, verbose_name = '이름')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=300, verbose_name = '이메일')  # Field name made lowercase.
    insert_day = models.DateField(db_column='INSERT_DAY', verbose_name = '가입일자')  # Field name made lowercase.
    coment = models.CharField(db_column='COMENT', max_length=500, blank=True, null=True, verbose_name = '하려는말')  # Field name made lowercase.



class Meta:
    managed = False
    db_table = 'user'

