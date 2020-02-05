from app_bookshelf.models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BookShelf, Like, History, BookShelfMaster, BookShelfRecomend

book_objs = []
for i in range(10000):
    try:
        book_objs.append(Book.objects.filter(id=i)[0])
    except:
        pass

for book_obj in book_objs:
    small_category_name = book_obj.small_category.small_category_name
    book_shelf_obj = BookShelfMaster.objects.filter(book_shelf_name=small_category_name)[0]
    BookShelf.objects.create(book=book_obj, book_shelf=book_shelf_obj)
