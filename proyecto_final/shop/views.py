from django.shortcuts import render

# Create your views here.
def pagina_online(request):
     return render(request,'prueba.html')


def about_pagina_online(request):
     parametros = {'numero_favorito': 77}
     return render(request,'about.html',parametros)
