from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stuffinfo(request):
    return render(request, 'stuffinfo.html')

def dept_setting(request):
    return render(request, 'dept_setting.html')

def proj_setting(request):
    return render(request, 'proj_setting.html')

def stuff_search(request):
    return render(request, 'stuff_search.html')