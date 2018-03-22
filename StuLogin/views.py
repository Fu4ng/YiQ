
from django.shortcuts import render, render_to_response

# Create your views here.

from django.template.loader import get_template
from django.contrib.auth import authenticate, login

from .models import *
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(id=username,pwd=password)

            if user:
                #登录成功
                #跳转到展示信息
                return render_to_response('StuLogin.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})

def stulogin(request):
    return redirect("http://www.baidu.com")