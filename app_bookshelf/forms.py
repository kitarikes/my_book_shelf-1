from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

# ユーザーに関するDB定義を持ってくる
from .models import CustomUser
# ユーザーの新規追加で使用する入力フォームの定義
class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'age', 'favorite_genre', 'keyword_1', 'keyword_2', 'keyword_3')


# 詳細画面でマイ本棚登録に使用するフォームの定義（※ボタンのみ）
from .models import Like
from django import forms
class LikeForm(forms.ModelForm):
	class Meta:
		model = Like
		fields = ()