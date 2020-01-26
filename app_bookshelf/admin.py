from django.contrib import admin
from .models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BookShelf, Like, History, BookShelfMaster, BookShelfRecomend

admin.site.register(CustomUser)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(LargeCategory)
admin.site.register(SmallCategory)
admin.site.register(Book)
admin.site.register(BookReviews)
admin.site.register(BookShelf)
admin.site.register(BookShelfMaster)
admin.site.register(BookShelfRecomend)
admin.site.register(Like)
admin.site.register(History)