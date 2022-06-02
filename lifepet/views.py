from django.shortcuts import render, get_object_or_404, redirect
from .models import Cadastro

def consultar(request):
    nome = request.GET.get("nome")
    if nome:
        consulta = Cadastro.objects.all().filter(nome__icontains=nome)
        return render(request, "cadastro/consultar.html", {"consulta":consulta})
    
    else:
        return render(request, "cadastro/consultar.html")

def search(request, id):
    consulta = get_object_or_404(Cadastro, pk=id)
    return render(request, "cadastro/search.html", {"consulta":consulta})
        
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
        especie = request.POST['especie']
        raca = request.POST['raca']
        porte = request.POST['porte']
        novo_cliente = Cadastro(nome=nome, nascimento=nascimento, email=email, telefone=telefone,local=local, numero=numero, bairro=bairro, cep=cep, obs=obs, especie=especie, raca=raca, porte=porte)
        novo_cliente.save()
        return redirect("/")
    else:
        return render(request, "cadastro/cadastro.html")
        
        
def editar(request, id):
    consulta = get_object_or_404(Cadastro, pk=id)
    if(request.method == "POST"):
        deletar(id)
    
    else:
        return render(request, "cadastro/editar.html", {"consulta":consulta})
    
    
    
def deletar(request, id):
    campo = get_object_or_404(Cadastro, pk=id)
    campo.delete()
    return redirect("/")