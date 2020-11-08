from django.core import validators
from django.db import models

#
# class TimeStamedModel(models.Model):
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name="가입날짜")
#     update_at = models.DateTimeField(auto_now_add=True, verbose_name="수정날짜")


class User(models.Model):
    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user_number = models.AutoField(db_column='USER_NUMBER', primary_key=True, verbose_name = '사용자명')
    id = models.CharField(db_column='ID',
                          max_length=50,
                          verbose_name = '아이디',
                          unique=True,
                          help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                          validators=[
                              validators.RegexValidator(
                                  r'^[\w.@+-]+$',
                                  'Enter a valid username. This value may contain only '
                                    'letters, numbers ' 'and @/./+/-/_ characters.'
                              ),
                            ],
                          error_messages={
                              'unique': "A user with that username already exists.",
                          }
                          )
    password = models.CharField(db_column='PASSWORD', max_length=50, verbose_name = '비밀번호')  # Field name made lowercase.
    user_name = models.CharField(db_column='NAME', max_length=10, verbose_name = '이름')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=300, verbose_name = '이메일',  unique=True)  # Field name made lowercase.
    coment = models.TextField(db_column='COMENT', max_length=2000, blank=True, null=True, verbose_name = '코멘트')  # Field name made lowercase.
    gender = models.CharField(blank=True, choices=GENDER_CHOICE, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255, verbose_name="전화번호")
    profile_photo = models.ImageField(blank=True, null=True, verbose_name="포토사진")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="가입날짜")
    update_at = models.DateTimeField(auto_now_add=True, null=True,  verbose_name="수정날짜")

    def __str__(self):
        return self.id

class Meta:
    managed = False
    db_table = 'user'
    ordering = ['-user_number']


