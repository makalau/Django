from django.shortcuts import render, get_object_or_404, redirect
from .models import Cadastro

def consultar(request):
    return render(request, 'cadastro/consultar.html')
    
def cadastro(request):
    if request.method == "POST":
        nome = request.POST['nome']
        nascimento = request.POST['nascimento']
        email = request.POST['email']
        telefone = request.POST['telefone']
        local = request.POST['local']
        numero = request.POST['numero']
        bairro = request.POST['bairro']
        cep = request.POST['cep']
        obs = request.POST['observation'] 
        novo_cliente = Cadastro(nome=nome, nascimento=nascimento, email=email, telefone=telefone,local=local, numero=numero, bairro=bairro, cep=cep, obs=obs)
        novo_cliente.save()
        return redirect("/")
    else:
        return render(request, "cadastro/cadastro.html")
    