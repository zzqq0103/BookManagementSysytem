# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-24 02:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20180624_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrator',
            old_name='admin_email',
            new_name='adminemail',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bookpublish_date',
            new_name='bookpublishdate',
        ),
        migrations.RenameField(
            model_name='bookborrow',
            old_name='borrow_date',
            new_name='borrowdate',
        ),
        migrations.RenameField(
            model_name='bookborrow',
            old_name='borrow_num',
            new_name='borrownum',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='useremail',
        ),
    ]
