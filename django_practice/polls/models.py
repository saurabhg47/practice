from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    """docstring for Model"""
    question_test = models.CharField(max_length=200)
    pub_dt = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_test

    def was_published_recently(self):
        return self.pub_dt >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.boolean = True
    was_published_recently.admin_order_field = 'pub_dt'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
