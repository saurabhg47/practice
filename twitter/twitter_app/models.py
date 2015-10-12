from django.db import models

class USER(models.Model):
    user_name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    # user_id = models.DateTimeField('date published')


class TWEET(models.Model):
    user = models.ForeignKey(USER)
    tweet_text = models.CharField(max_length=140)
    tweet_count = models.IntegerField(default=0)
    tweet_dt = models.DateTimeField('tweeted date')

class FOLLOWER(models.Model):
    user = models.ForeignKey(USER)
    follower_id = models.CharField(max_length=200)
    is_follow = models.CharField(max_length=1)
    follower_count = models.IntegerField(default=0)

class FOLLOWING(models.Model):
    user = models.ForeignKey(USER)
    following_id = models.CharField(max_length=200)
    is_following = models.CharField(max_length=1)
    following_count = models.IntegerField(default=0)

# Create your models here.
