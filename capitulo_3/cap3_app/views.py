from django.shortcuts import render
# Create your views here.

def home_page(request):
   return render(request, 'home.html')
def canelones(request):
   return render(request, 'index.html')

def carbonara(request):
   return render(request, 'Recetas/carbonara/index.html')

def ensaladilla_rusa(request):
   return render(request, 'recetas/ensaladilla_rusa/index.html')

def feijoada(request):
   return render(request, '/recetas/feijoada/index.html')

def flor_de_calabacin(request):
   return render(request, 'recetas/flor_de_calabacin/index.html')

def Gazpacho(request):
   return render(request, 'recetas/Gaspacho/index.html')

def mafe(request):
   return render(request, 'recetas/mafe/index.html')

def menu_infantil(request):
   return render(request, 'recetas/menu_infantil/index.html')

def pizza(request):
   return render(request, 'recetas/pizza/index.html')

def Receta_Facil(request):
    return render(request, 'recetas/receta_facil/index.html')
def sopa_de_noodles(request):
   return render(request, 'sopa_de_noodles/index.html')