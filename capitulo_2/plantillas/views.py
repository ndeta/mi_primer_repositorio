from django.shortcuts import render

import random

# Create your views here.
def home_page_view(request):
   return render(request, 'hola_mundo.html')



def ndeya_about(request):
   return render(request, 'about.html')

def about_page_view(request):
   parametros = {'numero_favorito':random.randrange(10)}


   return render(request, 'about.html', parametros)
