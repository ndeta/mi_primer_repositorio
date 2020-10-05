from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
import psycopg2
import psycopg2.extras

# Create your views here.
def formularios(request):

    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_6_user",
                            password="mango")
    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT * FROM Nota1 WHERE prioridad = '{prioridad}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    prioridad = request.GET.get('get_prioridad', default=None)
    with open("debug.log", "w") as debug_file:
        print(f"SELECT * FROM Nota1 WHERE prioridad LIKE '{prioridad}';", file=debug_file)

    params = {'notas': result}
    return render(request, 'formularios.html', params)


def anadir(request):

    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_6_user",
                            password="mango")


    cursor = conn.cursor()
    prioridad = request.POST["name_prioridad"]
    titulo= request.POST["nombre_titulo"]
    nota= request.POST["name_nota"]
    cursor.execute(f"INSERT INTO Nota1 VALUES ('{prioridad}','{titulo}','{nota}');")


    conn.commit()
    cursor.close()
    conn.close()

    return redirect('formularios')
