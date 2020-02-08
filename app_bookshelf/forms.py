from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

# ユーザーに関するDB定義を持ってくる
from .models import CustomUser
# ユーザーの新規追加で使用する入力フォームの定義
class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'age', 'favorite_genre', 'keyword_1', 'keyword_2', 'keyword_3')


