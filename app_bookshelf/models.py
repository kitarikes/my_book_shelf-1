from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# 会員情報マスタ
class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    gender = models.CharField('性別', max_length=255, blank=True, null=True)
    age = models.IntegerField('年齢', blank=True, null=True)
    favorite_genre = models.CharField('好きなジャンル', max_length=255, blank=True, null=True)
    keyword_1 = models.CharField('キーワード１', max_length=255, blank=True, null=True)
    keyword_2 = models.CharField('キーワード２', max_length=255, blank=True, null=True)
    keyword_3 = models.CharField('キーワード３', max_length=255, blank=True, null=True)


# 出版社マスタ
class Publisher(models.Model):
    class Meta:
        db_table = 'publisher_master'
        verbose_name_plural = '出版社マスタ'
        
    publisher_name = models.CharField('出版社名', max_length=255, blank=True, null=True)


# 著者マスタ
class Author(models.Model):
    class Meta:
        db_table = 'author_master'
        verbose_name_plural = '著者マスタ'
        
    author_name = models.CharField('著者名', max_length=255, blank=True, null=True)


# 大カテゴリマスタ
class LargeCategory(models.Model):
    class Meta:
        db_table = 'large_category_master'
        verbose_name_plural = '大カテゴリマスタ'
        
    learge_category_name = models.CharField('大カテゴリ名', max_length=255, blank=True, null=True)


# 小カテゴリマスタ
class SmallCategory(models.Model):
    class Meta:
        db_table = 'small_category_master'
        verbose_name_plural = '小カテゴリマスタ'
        
    learge_category = models.ForeignKey(LargeCategory, verbose_name='大カテゴリ(FK)', null=True, on_delete=models.CASCADE)
    small_catogory_name = models.CharField('小カテゴリ名', max_length=255, blank=True, null=True)


# 書籍マスタ
class Book(models.Model):
    class Meta:
        db_table = 'book_master'
        verbose_name_plural = '書籍マスタ'
        
    learge_category = models.ForeignKey(LargeCategory, verbose_name='大カテゴリ(FK)', null=True, on_delete=models.CASCADE)
    small_category = models.ForeignKey(SmallCategory, verbose_name='小カテゴリ(FK)', null=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社(FK)', null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, verbose_name='著者(FK)', null=True, on_delete=models.CASCADE)
    book_name = models.CharField('書籍名', max_length=255, blank=True, null=True)
    image_url = models.CharField('商品画像URL', max_length=255, blank=True, null=True)
    publish_date = models.DateTimeField('出版日')
    book_detail = models.CharField('書籍詳細', max_length=10000, blank=True, null=True)
    size_page = models.IntegerField('ページ数', blank=True, null=True)
    size_height = models.IntegerField('寸法（高さ）', blank=True, null=True)
    size_width = models.IntegerField('寸法（幅）', blank=True, null=True)
    isbn_10 = models.IntegerField('ISBN-10', blank=True, null=True)
    isbn_13 = models.IntegerField('ISBN-13', blank=True, null=True)
    purchase_page_url = models.CharField('購入ページURL', max_length=255, blank=True, null=True)


# 書籍レビューテーブル（複雑になるので、いったんER図には含めていない。Phase２で使用する）
class BookReviews(models.Model):
    class Meta:
        db_table = 'book_reviews_table'
        verbose_name_plural = '書籍レビューテーブル'
        
    book = models.ForeignKey(Book, verbose_name='書籍(FK)', null=True, on_delete=models.CASCADE)
    book_review = models.CharField('書籍レビュー', max_length=5000, blank=True, null=True)


# 本棚マスタ
class BoookShelf(models.Model):
    class Meta:
        db_table = 'book_shelf_master'
        verbose_name_plural = '本棚マスタ'
        
    learge_category = models.ForeignKey(LargeCategory, verbose_name='大カテゴリ(FK)', null=True, on_delete=models.CASCADE)
    small_catogory_name = models.CharField('小カテゴリ名', max_length=255, blank=True, null=True)


# いいねテーブル
class Like(models.Model):
    class Meta:
        db_table = 'like_table'
        verbose_name_plural = 'いいねテーブル'
        
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー(FK)', null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='書籍(FK)', null=True, on_delete=models.CASCADE)
    like_date = models.DateTimeField(default = timezone.now)


# 閲覧履歴テーブル
class History(models.Model):
    class Meta:
        db_table = 'history_table'
        verbose_name_plural = '閲覧履歴テーブル'
        
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー(FK)', null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='書籍(FK)', null=True, on_delete=models.CASCADE)
    history_date = models.DateTimeField(default = timezone.now)
