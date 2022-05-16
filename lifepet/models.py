from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=25)
    local = models.CharField(max_length=255)
    numero = models.CharField(max_length=4)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    obs = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    