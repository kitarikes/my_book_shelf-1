# Generated by Django 2.1.5 on 2020-02-05 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookshelf', '0007_bookshelfmaster_small_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookshelfmaster',
            name='small_category',
        ),
    ]