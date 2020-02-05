from app_bookshelf.models import CustomUser, Publisher, Author, LargeCategory, SmallCategory, Book, BookReviews, BookShelf, Like, History, BookShelfMaster, BookShelfRecomend
import pandas as pd

df = pd.read_csv('merged_data.csv')
columns = df.columns.tolist()

publisher_list = []
learge_category_list = []
small_category_list = []
author_list = []

for i in range(len(df)):
    if df.loc[i, '出版社'].split('(')[0].split(';')[0].split('/')[0].replace(' ', '') not in publisher_list:
        publisher_list.append(df.loc[i, '出版社'].split('(')[0].split(';')[0].split('/')[0].replace(' ', ''))
        
    if df.loc[i, '大カテゴリー'] not in learge_category_list:
        learge_category_list.append(df.loc[i, '大カテゴリー']) 
        
    if [df.loc[i, '大カテゴリー'], df.loc[i, '小カテゴリー']] not in small_category_list:
        small_category_list.append([df.loc[i, '大カテゴリー'], df.loc[i, '小カテゴリー']])
        
    if df.loc[i, '著者'] not in author_list:
        author_list.append(df.loc[i, '著者']) 

for publisher in publisher_list:
    Publisher.objects.create(publisher_name=publisher)


for learge_category in learge_category_list:
    LargeCategory.objects.create(learge_category_name=learge_category)

for author in author_list:
    Author.objects.create(author_name=author)

for small_category in small_category_list:
    learge_category_obj = LargeCategory.objects.get(learge_category_name=small_category[0])
    SmallCategory.objects.create(learge_category=learge_category_obj, small_category_name=small_category[1])

for small_category in small_category_list:
    small_category_obj = SmallCategory.objects.filter(small_category_name=small_category[1])[0]
    BookShelfMaster.objects.create(book_shelf_name=small_category[1])

