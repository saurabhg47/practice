# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FOLLOWER',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follower_id', models.CharField(max_length=200)),
                ('is_follow', models.CharField(max_length=1)),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FOLLOWING',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('following_id', models.CharField(max_length=200)),
                ('is_following', models.CharField(max_length=1)),
                ('following_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TWEET',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_text', models.CharField(max_length=140)),
                ('tweet_count', models.IntegerField(default=0)),
                ('tweet_dt', models.DateTimeField(verbose_name=b'tweeted date')),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='twitter_app.USER'),
        ),
        migrations.AddField(
            model_name='following',
            name='user',
            field=models.ForeignKey(to='twitter_app.USER'),
        ),
        migrations.AddField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(to='twitter_app.USER'),
        ),
    ]
