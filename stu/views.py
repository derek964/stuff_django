from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from stu.models import *
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST" and request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        userinfo = auth.authenticate(username=username, password=password)
        if userinfo:
            auth.login(request, userinfo)
            platinfo = platuser.objects.filter(platuser=username)
            if platinfo:
                return HttpResponseRedirect('/plat/')
            else:
                return HttpResponseRedirect('/index/')
        print(username, password)
        return redirect('/index')
    return render(request, 'login.html')

def index(request):
    stuffs_all = Stuff.objects.all()
    return render(request, 'index.html', context=locals())

def n1(request):
    # 产品线非zplan的
    stuffs_n1 = Stuff.objects.exclude(productname="zplan")
    return render(request, 'n1.html', context=locals())

def z1(request):
    # 产品线是zplan的
    stuffs_z1 = Stuff.objects.filter(productname="zplan")
    return render(request, 'z1.html', context=locals())

def plat(request):
    # 部门是mogs或yolo的
    stuffs_plat = Stuff.objects.filter(Q(deptname__deptcode='mogs')|Q(deptname__deptcode='yolo'))
    return render(request, 'plat.html', context=locals())

def game1(request):
    # 部门是游戏一组的
    stuffs_game1 = Stuff.objects.filter(deptname__deptcode='game1')
    return render(request, 'game1.html', context=locals())

def game2(request):
    # 部门是游戏二组的
    stuffs_game2 = Stuff.objects.filter(deptname__deptcode='game2')
    return render(request, 'game2.html', context=locals())

def art(request):
    # 部门是美术组的
    stuffs_art = Stuff.objects.filter(deptname__deptcode="art")
    return render(request, 'index.html', context=locals())