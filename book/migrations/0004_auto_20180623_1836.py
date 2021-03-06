# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-23 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180623_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='members',
            field=models.ManyToManyField(through='book.BookBorrow', to='book.User'),
        ),
        migrations.AddField(
            model_name='bookborrow',
            name='borrow_num',
            field=models.IntegerField(default=0, verbose_name='借书数量'),
        ),
    ]
