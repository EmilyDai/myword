# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
import datetime
@python_2_unicode_compatible
class Function(models.Model):
    name = models.CharField('功能', max_length=256,unique=True)
    slug = models.CharField('功能网址', max_length=256, db_index=True,unique=True)
    intro = models.TextField('功能简介', default='')
    nav_display = models.BooleanField('导航显示', default=True)
    home_display = models.BooleanField('首页显示', default=True) 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '功能'
        verbose_name_plural = '功能'
        ordering = ['name']  # 按照哪个栏目排序
        
    def get_absolute_url(self):
        return reverse('function', args=(self.slug,))
        
@python_2_unicode_compatible
class Column(models.Model):
    function = models.ManyToManyField(Function, verbose_name='归属功能')
    name = models.CharField('分类', max_length=256,unique=True)
    slug = models.CharField('分类网址', max_length=256,db_index=True,unique=True)
    intro = models.TextField('分类简介', default='')
#    nav_display = models.BooleanField('导航显示', default=False)
#    home_display = models.BooleanField('首页显示', default=False) 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        
    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))
 
 
@python_2_unicode_compatible
class Word(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属分类')
    name = models.CharField('单词', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)
#    comment = models.TextField('笔记', default='', blank=True)
#    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '单词'
        verbose_name_plural = '单词'
        
    def get_absolute_url(self):
        return reverse('word', args=(self.pk, self.slug))
    
@python_2_unicode_compatible        
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    column = models.CharField(default='六级',max_length=256)
    count = models.IntegerField(default=20)
    daka = models.IntegerField(default=0)
    date=models.DateField('时间',null=True,default=datetime.date(2012, 12, 7))
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    def __str__(self):
        return self.username
        

@python_2_unicode_compatible
class Comment(models.Model):
    wordfor = models.ManyToManyField(Word, verbose_name='归属单词')
    author = models.CharField('作者', max_length=50,)

    content = models.TextField('内容', default='', blank=True)
 
    def __str__(self):
        return self.content
 
    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = '笔记'