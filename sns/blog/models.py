# encoding:utf-8
from django.utils import timezone
from django.db import models

class Channel(models.Model):
    '''频道'''
    channel_name = models.CharField(u'频道名称', max_length=20)
    cover_img = models.CharField(u'频道图片', null=True, blank=True, max_length=255)
    order_index = models.IntegerField(u'排序', default=0)
    parent_id = models.IntegerField(u'父级', default=0)

    class Meta:
        verbose_name_plural = u'频道'
        verbose_name = u'频道'

class Article(models.Model):
    '''文章信息表'''
    title = models.CharField(max_length=255)  # 标题
    create_date = models.DateTimeField(default=timezone.now)  # 日期
    channel_id = models.IntegerField()  # 所属频道
    cover = models.CharField(max_length=500)  # 列表封面图片，多张一逗号分隔
    template = models.IntegerField()  # 列表显示风格模板：一张小图，一张大图，三联图
    remark = models.CharField(max_length=500) # 摘要
    content = models.TextField()  # 文章内容，如果是原创投稿，保存文章内容，如果是转载，只保存摘要
    is_original = models.BooleanField(default=False)  # 是否原创
    source = models.CharField(max_length=50)  # 如转载，保存文章来源
    user_id = models.IntegerField(default=0)  # 如原创投稿，保存投稿人ID,0表示系统转载
    user_name = models.CharField(max_length=50, null=True, blank=True)  # 冗余字段，保存投稿人姓名
    user_avatar = models.CharField(max_length=255)  # 冗余，用户头像
    status = models.IntegerField(default=0)  # 文章状态 0：草稿；1：发布；-1：删除
    comment_num = models.IntegerField(default=0)  # 评论数
    agree_num = models.IntegerField(default=0)  # 点赞数
    page_url = models.CharField(max_length=500)  # 原文链接
    update_date = models.DateTimeField(null=True, blank=True)

class Comment(models.Model):
    '''评论'''
    comment_content = models.CharField(max_length=255)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_avatar = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    agree_num = models.IntegerField(default=0)  # 点赞数
    article_id = models.IntegerField()  # 文章ＩＤ

class Tag(models.Model):
    article_id = models.IntegerField()
    tag_words = models.CharField(max_length=50)

class Favorite(models.Model):
    '''收藏'''
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    article_id = models.IntegerField()
    collect_date = models.DateTimeField(default=timezone.now)

class Subscribe(models.Model):
    '''我订阅的频道'''
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    channel_id = models.IntegerField()
    channel_name = models.CharField(max_length=50)