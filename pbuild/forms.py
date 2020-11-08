# from django import forms
from django import forms
from django.forms import Textarea

from .models import User
#
# class SingUpForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["id", 'password', 'user_name', 'email', 'gender', 'coment', 'phone_number']
#         labels = {
#             "id": '아이디',
#             "email": '이메일 주소',
#             'user_name': '성명',
#             'username': '사용자 이름',
#             'paswword': '비밀번호'
#         }
#         widgets = {
#             'name': Textarea(attrs={'cols':80, 'row': 20}),
#             'password': forms.PasswordInput(),
#             'eamil': forms.EmailInput
#         }
#
#         def save(self, commit=True):
#             # Save the provided password in hashed format
#             user = super().save(commit=False)
#             user.set_password(self.cleaned_data["password1"])
#             if commit:
#                 user.save()
#             return user
#


class SingUpForm(forms.Form):
    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id = forms.CharField(
        error_messages={"required":"먼가 적어볼래?"},
        label="아이디",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control col-7',

            }
        )
    )
    password = forms.CharField(
        label="비밀번호",
        widget= forms.PasswordInput(
            attrs={
                'class' : 'form-control col-7'
            }
        )
    )
    re_password = forms.CharField(
        label="비밀번호확인",
        widget= forms.PasswordInput(
            attrs={
                'class' : 'form-control col-7'
            }
        )
    )
    email = forms.EmailField(
        label="이메일",
        widget= forms.EmailInput(
            attrs={
                'class' : 'form-control col-7'
            }
        )
    )
    gender = forms.ChoiceField(
        label="성별",
        choices=GENDER_CHOICE,
        widget = forms.Select(
            attrs={
                'class' : 'form-control col-7'
            }
        )
    )
    coment = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control'
            }
        ),
        help_text="하고싶은 말을 적으세요"
    )
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(SingUpForm, self).clean()
        id = cleaned_data.get('id')
        password1 = cleaned_data.get('password')
        re_password= cleaned_data.get('re_password')
        user_name = cleaned_data.get('user_name')
        email = cleaned_data.get('email')
        gender = cleaned_data.get('gender')
        
        if not id:
            raise forms.ValidationError("뭐좀 적어라")
        if User.objects.filter(id=id).exists():
            raise forms.ValidationError("이미 사용중인 아이디 입니다.")
        if password1 != re_password:
            raise forms.ValidationError("비밀번호와 비밀번호 확의 값이 일치하지 않습니다.")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("이미 존재하는 이메일 입니다.")

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
                return user



    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #
    #     if not email.endswirh('@')

    # def clean_id(self):
    #     id = self.cleaned_data['id']
    #     if User.objects.filter(id=id).exists():
    #         print("이미 사용중인 아이디입니다.")
    #         raise forms.ValidationError("이미 사용중인 아이디 입니다.")
    #     return id
    # 
    #     def save(self, commit=True):
    #         # Save the provided password in hashed format
    #         user = super().save(commit=False)
    #         user.set_password(self.cleaned_data["password"])
    #         if commit:
    #             user.save()
    #         return user
    # 
    # def clean_password2(self):
    #     print(self.cleaned_data)
    #     password1 = self.cleaned_data['password']
    # 
    #     password2 = self.cleaned_data['password2']
    # 
    #     if password1 != password2:
    #         print('비밀번호와 비밀번호 확인의 값이 일치하지 않습니다.')
    #         raise forms.ValidationError('비밀번호와 비밀번호 확인의 값이 일치하지 않습니다.')
