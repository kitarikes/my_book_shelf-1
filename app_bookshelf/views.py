from django.shortcuts import render  
from django.views import View  
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BoookShelf, Like, History


class MyPage(LoginRequiredMixin, View):
        def get(self, request, *args, **kwargs):
                return render(request, 'app_bookshelf/my_page.html')
my_page = MyPage.as_view()

class MakeAccount(LoginRequiredMixin, View):  
        def get(self, request, *args, **kwargs):
                return render(request, 'app_bookshelf/make_account.html')
make_account= MakeAccount.as_view()

class AccountEdit(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/account_edit.html')
account_edit = AccountEdit.as_view()

class Login(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/login.html')
login = Login.as_view()

class ShelfSearch(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/shelf_search.html')
shelf_search = ShelfSearch.as_view()

class ShelfList(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/shelf_list.html')
shelf_list = ShelfList.as_view()

class BrowsingHistory(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/browsing_history.html')
browsing_history = BrowsingHistory.as_view()

class LikeHistory(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/like_history.html')
like_history = LikeHistory.as_view()

class BookShelfs(LoginRequiredMixin, View):  
   def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/book_shelfs.html')
book_shelfs = BookShelfs.as_view()

class BookDetails(LoginRequiredMixin, View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_bookshelf/book_details.html')
book_details = BookDetails.as_view()