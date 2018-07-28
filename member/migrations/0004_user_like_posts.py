# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-27 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('member', '0003_auto_20180727_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='post.Post'),
        ),
    ]
