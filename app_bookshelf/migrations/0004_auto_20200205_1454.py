# Generated by Django 2.1.5 on 2020-02-05 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookshelf', '0003_auto_20200205_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smallcategory',
            old_name='small_catogory_name',
            new_name='small_category_name',
        ),
    ]
