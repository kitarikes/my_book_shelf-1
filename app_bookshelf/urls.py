from django.urls import path
from . import views

app_name = 'app_bookshelf'
urlpatterns = [
    path('my_page/', views.my_page, name='my_page'),
    path('make_account/', views.make_account, name='make_account'),
    path('account_edit/', views.account_edit, name='account_edit'),
    path('login/', views.login, name='login'),
    path('shelf_search/', views.shelf_search, name='shelf_search'),
    path('shelf_list/', views.shelf_list, name='shelf_list'),
    path('browsing_history/', views.browsing_history, name='browsing_history'),
    path('like_history/', views.like_history, name='like_history'),
    path('book_shelfs/', views.book_shelfs, name='book_shelfs'),
    path('book_details/', views.book_details, name='book_details'),
    ]