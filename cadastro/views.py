from django.shortcuts import render, get_object_or_404
from .models import Cadastro

def consultar(request):
    return render(request, 'cadastro/consultar.html')
    
def cadastro(request):
    context = {}
    if request.method == "POST":
        erros = {}
        nome = request.POST.get('nome', None)
        if nome != "Marcelo":
            erros["nome"] = "O nome é diferente do esperado"
        
        if erros:
            context['erros']  = erros 
        else:
            print("Salvando os dados")
            context["msg"] = "Os dados foram salvos com sucesso"
    return render(request, "cadastro/cadastro.html", context=context)