from django.shortcuts import render,HttpResponse

# Create your views here.
def formularios(request):
    return render(request, 'formularios.html')
def anadir(request):
    prioridad = request.POST["name_prioridad"]
    return(HttpResponse(f'Insertado <br> '
                        f'prioridad: {prioridad }<br>'))
