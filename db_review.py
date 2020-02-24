import pandas as pd
import re
from app_bookshelf.models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BookShelf, Like, History, BookShelfMaster, BookShelfRecomend
df = pd.read_csv('merged_review.csv')
error_list = []
for i in range(len(df)):
    try:
        url = df.iloc[i, 0]
        book_object = Book.objects.filter(purchase_page_url = url)[0]
        text = df.iloc[i, 1]
        star = df.iloc[i, 2]
        BookReviews.objects.create(
        book = book_object,
        book_review = text,
        book_review_star = star
        )
    except:
        error_list.append(i)