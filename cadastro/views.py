from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    hora = datetime.datetime.now()
    html = "<html><body>Agora eh: %s.</body></html>" %hora
    return HttpResponse(hora)
