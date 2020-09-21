from django.shortcuts import render,HttpResponse
import psycopg2

# Create your views here.
def formularios(request):
    return render(request, 'formularios.html')
def anadir(request):

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="mango")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO nota VALUES ('total','coregir_examenes', \
                       'examenes_uf3_lunes');")
    cursor.execute("select * from nota")
    return HttpResponse(cursor.fetchall())

    return HttpResponse('registros insertados')