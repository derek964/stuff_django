from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def n1(request):
    return render(request, 'n1.html')

def z1(request):
    return render(request, 'z1.html')

def plat(request):
    return render(request, 'plat.html')

def game1(request):
    return render(request, 'game1.html')

def game2(request):
    return render(request, 'game2.html')

def art(request):
    return render(request, 'index.html')