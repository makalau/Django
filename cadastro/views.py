from django.shortcuts import render

def home(request):
    return render(request, 'cadastro\home.html')

def cadastro(request):
    return render(request, "cadastro\cadastro.html")