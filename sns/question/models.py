# encoding:utf-8
from django.db import models

# Create your models here.
class Question(models.Model):
    '''问题'''
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_avatar = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    has_accepted_answer = models.BooleanField(default=False)

class Answer(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_avatar = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    voites = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=False)

class Tag(models.Model):
    answer_id = models.IntegerField()
    tag_words = models.CharField(max_length=50)

