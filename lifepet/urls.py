from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultar, name='consultar'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
