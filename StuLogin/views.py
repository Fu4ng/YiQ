
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


class RepairForm(forms.Form):
    fid = forms.CharField(label='设备ID', max_length=20)
    id = forms.CharField(label='学生ID', max_length=50)
    text = forms.CharField(label='报修内容<br>',widget=forms.Textarea)


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
    return render_to_response('login.html')

def repair(request):
    if request.method == 'POST':
        repairform = RepairForm(request.POST)
        if repairform.is_valid():
            fid = repairform.cleaned_data['fid']
            id = repairform.cleaned_data['id']
            # 对id和fid 验证
            f = Facility.objects.get(fid = fid)
            u = User.objects.get(id = id)
            if f and u:
                text = repairform.cleaned_data['text']
                repairData = WRecords.objects.create(fid=fid,id=id,text=text)
                print(type(repairData), repairData)
                return HttpResponse("报修成功")
            else:
                return HttpResponse("设备ID或学生ID不存在")
    else:
        repairform = RepairForm()
    return render_to_response('repair.html')
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