from django.db import models

class Cadastro(models.Model):
    nome = models.TextField(max_length=50)
    nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.TextField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    