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
        #book_shelfs = BookShelfMaster.objects.all()
        #BookShelfMasterが本棚マスタ

        #template form/input/name"SearchWordfromShelf"の値を取得する
        searchword = request.POST.get("ShelfSearchWord")
        #print (searchword)
        #getできなかったらNONEが帰ってくるので、すべて検索する
        if  searchword is None:
            book_shelfs = BookShelfMaster.objects.all()
        else:
            book_shelfs = BookShelfMaster.objects.filter(book_shelf_name__icontains= searchword)
        
        #print (request.POST.get("SearchWordfromShelf","default"))
        #並び替えとか追加

        # HTMLに変数を渡す
        context = {'book_shelfs':book_shelfs}
        
        return render(request, 'app_bookshelf/shelf_list.html', context=context)

shelf_search = ShelfSearch.as_view()


# 本棚
class BookShelfs(LoginRequiredMixin, View):  
   def post(self, request, *args, **kwargs):
        print(request.POST.get("result_pk"))
        book_shelf_id = int(request.POST.get("result_pk"))

        book_shelf_name = BookShelfMaster.objects.get(id = book_shelf_id)
       # 選択された本棚に紐づく書籍オブジェクトを取得
        book_objects = BookShelf.objects.filter(book_shelf__id = book_shelf_id)

       # 書籍オブジェクト１つ１つから書籍IDを取得（for文つかう）
        books_id = []
        for i in book_objects:
            books_id.append(i.book_id)

       # 書籍DBから書籍情報を検索（書籍IDを使う）
        books = Book.objects.filter(id__in=books_id)
        context = {'books':books, 'book_shelf_name':book_shelf_name}

        return render(request, 'app_bookshelf/book_shelfs.html', context=context)


   def get(self, request, *args, **kwargs): 
       # すべての書籍オブジェクトを取得
       book_objects = BookShelf.objects.all()

       # 書籍オブジェクト１つ１つから書籍IDを取得（for文つかう）
       books_id = []
       counter = 0
       for i in book_objects:
           books_id.append(i.book_id)
           counter += 1
           if counter == 100:
               break

       # 書籍DBから書籍情報を検索（書籍IDを使う）
       books = Book.objects.filter(id__in=books_id)
       context = {'books':books}

       return render(request, 'app_bookshelf/book_shelfs.html', context=context)
book_shelfs = BookShelfs.as_view()

# 本の詳細ページ
class BookDetails(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        input_data = int(request.POST.get("book_id"))

        result1 = Book.objects.get(id=input_data)
        result2 = BookReviews.objects.filter(id=input_data).first()

        context = {'result1':result1, 'result2':result2}
        return render(request, 'app_bookshelf/book_details.html', context=context)
book_details = BookDetails.as_view()


# 閲覧履歴
from django.db.models import Q
from django.core.paginator import Paginator

class BrowsingHistory(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        q_word = self.request.GET.get('query')
        browsing_history= History.objects.filter(user__id = request.user.id)

        # 閲覧履歴の検索（書籍名と著者名） ＊複数検索ボックスは未実装
        if q_word:
            object_list = browsing_history.filter(
                Q(book__book_name__icontains=q_word) | Q(book__author__author_name__icontains=q_word))
        else:
            object_list = browsing_history

      # ページネーション
        paginator = Paginator(object_list, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'browsing_history':browsing_history, 'object_list':object_list, 'page_obj':page_obj}
        return render(request, 'app_bookshelf/browsing_history.html', context=context) 

browsing_history = BrowsingHistory.as_view()


# いいねリスト
from datetime import datetime

class LikeHistory(LoginRequiredMixin, View):  
    def get(self, request, *args, **kwargs):

        # 閲覧履歴の一覧
        like_history= Like.objects.filter(user__id = request.user.id)

        # ページネーション
        paginator = Paginator(like_history, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # HTMLに変数を渡す
        context = {'like_history':like_history, 'page_obj': page_obj,}
        return render(request, 'app_bookshelf/like_history.html', context =context)


    # いいね削除の処理
    def post(self, request, *args, **kwargs):
        item_pks = request.POST.getlist('delete')
        Like.objects.filter(user__id = request.user.id, pk__in=item_pks).delete()
        
        return redirect('app_bookshelf:like_history')

like_history = LikeHistory.as_view()