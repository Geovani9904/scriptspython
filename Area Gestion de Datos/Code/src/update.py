import psycopg2

def updateTable(useraccount, password):
    try:
        conn = psycopg2.connect(user="postgres",
                                      password="metal3D",
                                      host="10.60.63.106",
                                      port="5432",
                                      database="api")

        cursor = conn.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from useraccount where id = %s"""
        cursor.execute(sql_select_query, (useraccount,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update useraccount set password = %s where id = %s"""
        cursor.execute(sql_update_query, (password, useraccount))
        conn.commit()
        count = cursor.rowcount
        print(count, "Se actualizo correctamente ")

        print("Los datos modificados antes de ")
        sql_select_query = """select * from useraccount where id = %s"""
        cursor.execute(sql_select_query, (useraccount,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar la operacion", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL conexion esta cerrado")

useraccount = 3
password = 123456
updateTable(useraccount, password)
