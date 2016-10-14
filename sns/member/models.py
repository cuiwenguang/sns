# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''会员扩展信息'''
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50, null=True, blank=True) # 所在地
    avatar = models.CharField(max_length=255,  null=True, blank=True) # 头像
    job = models.CharField(max_length=50, null=True, blank=True) # 工作
    mobile = models.CharField(max_length=20, null=True, blank=True) # 电话
    integral = models.IntegerField(default=0) # 资产（积分）
    is_temp = models.BooleanField(default=True) # 是否零时会员，即游客，gust账户
    provider = models.CharField(max_length=20, default='local') # 登录方式

class Friend(models.Model):
    user_id = models.IntegerField()
    follow_id = models.IntegerField()



