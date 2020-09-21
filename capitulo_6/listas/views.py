from django.shortcuts import render,HttpResponse
import psycopg2

# Create your views here.
def formularios(request):
    return render(request, 'formularios.html')
def anadir(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]


    return(HttpResponse(f'Insertado <br> '
                        f'prioridad: {prioridad }<br>'
                        f'titulo: {titulo}<br>'
                        f'nota: {nota}<br>'))
