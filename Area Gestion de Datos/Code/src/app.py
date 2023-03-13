import psycopg2


class bcolors:
    OK = '\033[92m' #GREEN,
    FAIL = '\033[91m' #RED

DB_NAME = "api"
DB_USER = "postgres"
DB_PASSWORD = "metal3D"
DB_HOST = "10.60.63.106"
DB_PORT = "5432"


try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cursor = conn.cursor()
    postgres_insert_query = """ INSERT INTO useraccount (id, username, password) VALUES (%s,%s,%s)"""
    record_to_insert = (5, 'Gio', '123456789')
    cursor.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    count = cursor.rowcount
    print(count, "Se inserto correctamente")

    print(bcolors.OK + "Conexion exitosa")
    cursor.execute("SELECT * FROM useraccount")
    datos = cursor.fetchall()
    print(datos)
except (Exception, psycopg2.Error) as error:
    print ("Error al conectarse al server", error) 
    conn.close()

# finally:
#     # closing database connection.
#     if conn:
#         cursor.close()
#         conn.close()
#         print("PostgreSQL conexion esta cerrado")
