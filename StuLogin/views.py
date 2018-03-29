
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

            user = User.objects.get(id=username,pwd=password)

            if user:
                #登录成功
                #跳转到展示信息
                if(user.type== 1): #如果用户是学生的话
                    return redirect('http://127.0.0.1:8000/showInfo/'+username)
                elif(user.type==2): #如果用户是管理员的话，跳转到设备界面
                    return redirect('http://127.0.0.1:8000/facility/')
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})

def showInfo(request,id):
    template = get_template('showInfo.html')
    u=User.objects.get(id=id)
    html = template.render(locals())
    return HttpResponse(html)

def showFacility(request):
    template = get_template('showFacility.html')
    f_list = Facility.objects.all()
    html = template.render(locals())
    return HttpResponse(html)
def facilityDetail(request,fid):
    t = get_template('facilityDetail.html')
    try:
        f=Facility.objects.get(fid=fid)
        if f != None:
            html = t.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def showComment(request,fid):
    template = get_template('showComment.html')
    c_list = Comment.objects.filter(fid=fid)
    html = template.render(locals())
    return HttpResponse(html)

def stulogin(request):
    return redirect("http://www.baidu.com")