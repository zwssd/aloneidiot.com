# coding=utf-8

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='名字')
    email = models.CharField(max_length=50, verbose_name='email')
    passwd = models.CharField(max_length=50, verbose_name='密码')
    admin = models.BooleanField(verbose_name='是否是管理员')
    image = models.CharField(max_length=255, verbose_name='用户图片')
    create_time = models.DateTimeField(verbose_name='创建时间')
    edit_time = models.DateTimeField(verbose_name='编辑时间')
    def __str__(self):
        return self.name

class Content(models.Model):
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间')
    edit_time = models.DateTimeField(verbose_name='编辑时间')
    def __str__(self):
        return self.content

class Category(models.Model):
    cname = models.CharField(max_length=50, verbose_name='栏目名')
    def __str__(self):
        return self.cname

class Nav(models.Model):
    title = models.CharField(max_length=50, verbose_name='导航栏标题')
    parent = models.IntegerField(verbose_name='上一级导航栏id')
    url = models.CharField(max_length=255, verbose_name='导航栏地址')
    sort = models.IntegerField(default=0,verbose_name='导航栏排序')
    #外键
    articles = models.ForeignKey('Articles', on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title

class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    summary = models.CharField(max_length=100, verbose_name='文章摘要')
    imgurl = models.CharField(max_length=255, verbose_name='图片地址')
    tag = models.CharField(max_length=50, verbose_name='文章标签')
    top = models.BooleanField(verbose_name='是否置顶')
    create_time = models.DateTimeField(verbose_name='创建时间')
    edit_time = models.DateTimeField(verbose_name='编辑时间')
    #外键
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title



class Comments(models.Model):
    content = models.CharField(max_length=255, verbose_name='评论内容')
    ip = models.CharField(max_length=50, verbose_name='评论IP')
    create_time = models.DateTimeField(verbose_name='创建时间')
    edit_time = models.DateTimeField(verbose_name='编辑时间')
    #外键
    articles = models.ForeignKey('Articles', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.content
