# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from learn.models import Column,Word,Function,User,Comment
from learn.forms import CommentForm
import datetime

def index(request):
    home_display_functions = Function.objects.filter(home_display=True)
    nav_display_functions = Function.objects.filter(nav_display=True)
    username,flag=get_session(request)
    return render(request, 'index.html', {
        'home_display_functions': home_display_functions,
        'nav_display_functions': nav_display_functions,
        'flag':flag,
        'username':username
    })

def get_session(request):
    flag=False
    if 'user_name' in request.session:
        username=request.session["user_name"]
        flag=True
    else:
        username=''
    return username,flag

class ColumnForm(forms.Form):
    column=forms.CheckboxInput()
    count=forms.CharField()

    
def function_detail(request, function_slug):
    function = Function.objects.get(slug=function_slug)
    username,flag=get_session(request)
    user=None
    cf=''
    count_list=[50,100,150]
    if flag:
        user = User.objects.get(username__exact = username)
        if request.method == 'POST':
#            cf = ColumnForm(request.POST)
#            if cf.is_valid():
            new_column = request.POST['choice']
            new_count = request.POST['count']
            user.column=new_column
            user.count=new_count
            user.save()
        else:
            cf = ColumnForm()
    home_display_functions = Function.objects.filter(home_display=True)
    nav_display_functions = Function.objects.filter(nav_display=True)
    return render(request, 'learn/function.html', {'function': function,
                                                   'user':user,
                                                   'flag':flag,
                                                   'cf':cf,
                                                   'username':username,
                                                   'count_list':count_list,
                                                 'home_display_functions': home_display_functions,
                                                 'nav_display_functions': nav_display_functions,})
 
def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    username,flag=get_session(request)
    home_display_functions = Function.objects.filter(home_display=True)
    nav_display_functions = Function.objects.filter(nav_display=True)
    return render(request, 'learn/column.html', {'column': column,
                                                 'flag':flag,
                                                 'username':username,
                                                 'home_display_functions': home_display_functions,
                                                 'nav_display_functions': nav_display_functions,})
 
 
def word_detail(request, pk, word_slug):
    word = Word.objects.get(pk=pk)
    username,flag=get_session(request)
    comment_all=Comment.objects.filter(wordfor= word)
    comment_my=Comment.objects.filter(wordfor= word,author=username)
    home_display_functions = Function.objects.filter(home_display=True)
    nav_display_functions = Function.objects.filter(nav_display=True)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            
            a = comment.cleaned_data['comment']
            comment=Comment.objects.get_or_create(author=username,content=a)[0]
            comment.wordfor.add(word)

#            return render(request, 'learn/word.html', {'word': word,
#                                                   'form': comment,
#                                                   'comment_all':comment_all,
#                                                   'comment_my':comment_my,
#                                                   'home_display_functions': home_display_functions,
#                                                   'nav_display_functions': nav_display_functions,})
    else:
        comment = CommentForm()
    return render(request, 'learn/word.html', {'word': word,
                                               'form': comment,
                                               'comment_all':comment_all,
                                               'comment_my':comment_my,
                                               'flag':flag,
                                               'username':username,
                                               'home_display_functions': home_display_functions,
                                               'nav_display_functions': nav_display_functions,})

def bdc(request):
    home_display_functions = Function.objects.filter(home_display=True)
    nav_display_functions = Function.objects.filter(nav_display=True)
    username,flag=get_session(request)    
    if flag:
        daka_flag=False
        user = User.objects.get(username__exact = username)
        column_name=user.column
        count=user.count
        daka=user.daka
        column = Column.objects.get(name=column_name)
        words=column.word_set.all()[daka*count:(daka+1)*count]
        if (datetime.date.today()-user.date).days<1:
            daka_flag=True
            
        else:
            daka_flag=False
        if request.method == 'POST':
            user.daka=user.daka+1
            user.date=datetime.date.today()
            user.save()
            daka_flag=True
        return render(request, 'learn/bdc.html', {'words': words,
                                                  'count':count,
                                                  'daka_flag':daka_flag,
                                                  'flag':flag,
                                                 'username':username,
                                                 'home_display_functions': home_display_functions,
                                                 'nav_display_functions': nav_display_functions,})                                                 


def reset(request, function_slug):
    function = Function.objects.get(slug=function_slug)
    username,flag=get_session(request)
    user=None
    cf=''
    count_list=[50,100,150]
    if flag:
        user = User.objects.get(username__exact = username)
        if request.method == 'POST':
#            cf = ColumnForm(request.POST)
#            if cf.is_valid():
            new_column = request.POST['choice']
            new_count = request.POST['count']
            user.column=new_column
            user.count=new_count
            user.save()
        else:
            cf = ColumnForm()
    home_display_functions = Function.objects.filter(home_display=True)
    nav_display_functions = Function.objects.filter(nav_display=True)
    return render(request, 'learn/reset.html', {'function': function,
                                                   'user':user,
                                                   'flag':flag,
                                                 'username':username,
                                                   'cf':cf,
                                                   'count_list':count_list,
                                                 'home_display_functions': home_display_functions,
                                                 'nav_display_functions': nav_display_functions,})
                                                 
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())



def regist(request):

    nav_display_functions = Function.objects.filter(nav_display=True)
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.get_or_create(username= username,password=password)
            return HttpResponseRedirect('/accounts/login/')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf,'nav_display_functions': nav_display_functions,}, context_instance=RequestContext(request))


def login(request):
    nav_display_functions = Function.objects.filter(nav_display=True)
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
#            m = User.objects.get(username=request.POST['username'])
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/')
                #将username写入浏览器cookie,失效时间为3600
#                response.set_cookie('username',username,3600)
                request.session['user_name'] = username
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/accounts/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf,'nav_display_functions': nav_display_functions,},context_instance=RequestContext(request))


def logout(request):
    try:
        del request.session['user_name']
    except KeyError:
        pass
#    return HttpResponse("You're logged out.")
    return HttpResponseRedirect('/accounts/login/')