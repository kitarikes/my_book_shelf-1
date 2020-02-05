from django.shortcuts import render  
from django.views import View  
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BookShelf, Like, History, BookShelfMaster, BookShelfRecomend

from .func_1 import class_1 # ファイル名　クラス名

# 会員登録ページ
class MakeAccount(LoginRequiredMixin, View):  
    def get(self, request, *args, **kwargs):
        return render(request, 'app_bookshelf/make_account.html')
make_account= MakeAccount.as_view()


# 会員情報変更
class AccountEdit(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/account_edit.html')
account_edit = AccountEdit.as_view()


# マイページ
class MyPage(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # DBからユーザ情報を取得
        username = request.user.username
        gender = request.user.gender
        age = request.user.age
        favorite_genre = request.user.favorite_genre
        keyword_1 = request.user.keyword_1
        keyword_2 = request.user.keyword_2
        keyword_3 = request.user.keyword_3

        # HTMLに変数を渡す
        context = {'username':username, 'gender':gender,
        'age':age, 'favorite_genre':favorite_genre,
        'keyword_1':keyword_1, 'keyword_2':keyword_2, 'keyword_3':keyword_3}

        # HTMLを表示させる
        return render(request, 'app_bookshelf/my_page.html', context=context)

my_page = MyPage.as_view()


# 本棚検索ページ
class ShelfSearch(LoginRequiredMixin, View):  
    # 検索窓と、おススメ一覧（）
    def get(self, request, *args, **kwargs):        
        # おススメ本棚の一覧
        recomend_book_shelfs=BookShelfRecomend.objects.filter(user__id = request.user.id)
        # HTMLに変数を渡す
        context = {'recomend_book_shelfs':recomend_book_shelfs}

        return render(request, 'app_bookshelf/shelf_search.html', context=context)

    # 本棚の検索結果
    def post(self, request, *args, **kwargs):
        # 本棚から情報を取得（いったん全部検索する）
        book_shelfs = BookShelf.objects.all()
        # HTMLに変数を渡す
        context = {'book_shelfs':book_shelfs}

        return render(request, 'app_bookshelf/shelf_list.html', context=context)

shelf_search = ShelfSearch.as_view()


# 本棚
class BookShelfs(LoginRequiredMixin, View):  
   def post(self, request, *args, **kwargs): 
       # 検索画面で選択された本棚情報（ID番号）を取得
       book_shelf_id = 1 #← POSTで画面から受け取る様に変更する

       # 選択された本棚に紐づく書籍オブジェクトを取得
       book_objects = BookShelf.objects.filter(book_shelf__id = book_shelf_id)
       # 書籍オブジェクト１つ１つから書籍IDを取得（for文つかう）

       # 書籍DBから書籍情報を検索（書籍IDを使う）


       context = {'books':books}

       return render(request, 'app_bookshelf/book_shelfs.html', context=context)
book_shelfs = BookShelfs.as_view()


# 本の詳細ページ
class BookDetails(LoginRequiredMixin, View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/book_details.html')
book_details = BookDetails.as_view()


# 閲覧履歴
class BrowsingHistory(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/browsing_history.html')
browsing_history = BrowsingHistory.as_view()


# いいねリスト
class LikeHistory(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/like_history.html')
like_history = LikeHistory.as_view()


