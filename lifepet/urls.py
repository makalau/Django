from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultar, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path("consultar/", views.consultar, name="consultar"),
    path("deletar/", views.deletar, name="deletar"),
    path("search/<int:id>", views.search, name="search"),
]
