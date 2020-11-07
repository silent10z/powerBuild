# from django import forms
from django import forms as djnaog_forms
from .models import User
#
class SingUpForm(djnaog_forms.ModelForm):
    class Meta:
        model = User
        fields = ["id", 'password', 'user_name', 'email', 'gender', 'coment', 'phone_number']

        labels = {
            "id": '아이디',
            "email": '이메일 주소',
            'name': '성명',
            'username': '사용자 이름',
            'paswword': '비밀번호'
        }

        widgets = {
            'password': djnaog_forms.PasswordInput(),
        }

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user