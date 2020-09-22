from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
import psycopg2

# Create your views here.
def formularios(request):

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="mango")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Nota;")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'formularios.html', params)


def anadir(request):

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="mango")
    cursor = conn.cursor()
    prioridad = request.POST["name_prioridad"]
    titulo= request.POST["nombre_titulo"]
    nota= request.POST["name_nota"]
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}','{titulo}','{nota}');")


    conn.commit()
    cursor.close()
    conn.close()

    return redirect('formularios')
