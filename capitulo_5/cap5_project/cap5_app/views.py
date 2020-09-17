import psycopg2

def insert(request):
   conn = psycopg2.connect(dbname="capitulo_4_db",
                           user="capitulo_4_user",
                           password="patata")

   cursor = conn.cursor()
   cursor.execute("INSERT INTO emp VALUES)