from django.shortcuts import render
from stu.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stuffinfo(request):
    stuffinfos = stuff.objects.all()
    return render(request, 'stuffinfo.html', context=locals())

def dept_setting(request):
    return render(request, 'dept_setting.html')

def proj_setting(request):
    return render(request, 'proj_setting.html')

def stuff_search(request):
    return render(request, 'stuff_search.html')