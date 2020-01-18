from django.contrib import admin
from .models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BoookShelf, Like, History

admin.site.register(CustomUser)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(LargeCategory)
admin.site.register(SmallCategory)
admin.site.register(Book)
admin.site.register(BookReviews)
admin.site.register(BoookShelf)
admin.site.register(Like)
admin.site.register(History)