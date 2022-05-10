from django.shortcuts import render, get_object_or_404
from .models import Cadastro

def consultar(request):
    return render(request, 'cadastro/consultar.html')
    
def cadastro(request):
    
    return render(request, "cadastro/cadastro.html")