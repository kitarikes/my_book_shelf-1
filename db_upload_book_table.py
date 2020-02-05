from app_bookshelf.models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BookShelf, Like, History, BookShelfMaster, BookShelfRecomend
import pandas as pd

df = pd.read_csv('merged_data.csv')
columns = df.columns.tolist()


for i in range(len(df)):
    try:
        publisher = df.loc[i, columns[6]].split('(')[0].split(';')[0].split('/')[0].replace(' ', '')
        publisher_obj = Publisher.objects.filter(publisher_name=publisher)[0]
        learge_category = df.loc[i, columns[7]]
        learge_category_obj = LargeCategory.objects.filter(learge_category_name=learge_category)[0]
        small_category = df.loc[i, columns[9]]
        small_category_obj = SmallCategory.objects.filter(small_category_name=small_category)[0]
        author = df.loc[i, columns[12]]
        author_obj = Author.objects.filter(author_name=author)[0]
        
        isbn_10 = df.loc[i, columns[0]]
        isbn_13 = df.loc[i, columns[1]]
        purchase_page_url = df.loc[i, columns[2]]
        book_name = df.loc[i, columns[3]]
        size_page = df.loc[i, columns[4]]
        price = df.loc[i, columns[5]]
        image_url = df.loc[i, columns[10]]
        publish_date = df.loc[i, columns[11]]
        book_detail = df.loc[i, columns[13]]
        

        Book.objects.create(
            learge_category = learge_category_obj,
            small_category = small_category_obj,
            publisher = publisher_obj,
            author = author_obj,
            price = price,
            book_name = book_name,
            image_url = image_url,
            publish_date = publish_date,
            book_detail = book_detail,
            size_page = size_page,
            isbn_10 = isbn_10,
            isbn_13 = isbn_13,
            purchase_page_url = purchase_page_url
        )   
         
    except:
        pass