from django import forms
from .models import User


def min_length_3_validator(value):
    if len(value) < 4:
        raise forms.ValidationError('4글자 이상 입력해주세요')

class SingUpForm(forms.Form):

    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id = forms.CharField(
        validators=[min_length_3_validator],
        label="아이디",
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control col-7',

            }
        ),

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
    user_name = forms.CharField(
        label= "이름",
        widget= forms.TextInput(
            attrs={

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
                'class' : 'form-control',
                "required" : "False"
            }
        ),
        help_text="하고싶은 말을 적으세요"
    )



    def clean(self):
        cleaned_data = super(SingUpForm, self).clean()
        id = cleaned_data.get('id')
        password = cleaned_data.get('password')
        re_password= cleaned_data.get('re_password')
        user_name = cleaned_data.get('user_name')
        email = cleaned_data.get('email')
        gender = cleaned_data.get('gender')


        if not user_name:
            raise forms.ValidationError("사용자 이름을 적으세요")
        if User.objects.filter(id=id).exists():
            raise forms.ValidationError("이미 사용중인 아이디 입니다.")
        if password != re_password:
            raise forms.ValidationError("비밀번호와 비밀번호 확의 값이 일치하지 않습니다.")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("이미 존재하는 이메일 입니다.")

    def save(self, commit=True):
        user = User()
        cleaned_data = super(SingUpForm, self).clean()
        user.id = cleaned_data.get('id')
        user.user_name = cleaned_data.get("user_name")
        user.password = cleaned_data.get('password')
        user.email = cleaned_data.get('email')
        user.gender = cleaned_data.get('gender')
        user.coment = cleaned_data.get("coment")

        if commit:
            user.save()
        return user





