import mysql.connector

conexion = mysql.connector.connect(user='root', password='mysql',
                                    host='localhost',
                                    database='world',
                                    port='3306')

print(conexion)

miCursor = conexion.cursor()

miCursor.execute("SHOW DATABASES")

consulta = miCursor.fetchall()

print(consulta)