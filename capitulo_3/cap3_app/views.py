from django.shortcuts import render
# Create your views here.

def home_page(request):
   return render(request, 'home.html')
def canelones(request):
   return render(request, 'index.html')

def carbonara(request):
   return render(request, 'index.html')

def ensaladilla_rusa(request):
   return render(request, 'index.html')

def feijoada(request):
   return render(request, 'index.html')

def flor_de_calabacin(request):
   return render(request, 'index.html')

def Gazpacho(request):
   return render(request, 'index.html')

def mafe(request):
   return render(request, 'index.html')

def menu_infantil(request):
   return render(request, 'index.html')

def pizza(request):
   return render(request, 'index.html')

def Receta_Facil(request):
    return render(request, 'index.html')
def sopa_de_noodles(request):
   return render(request, 'index.html')