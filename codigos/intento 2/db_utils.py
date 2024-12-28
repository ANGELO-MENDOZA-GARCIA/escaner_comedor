import pymysql

# Configura la conexión con tu base de datos (ajusta los parámetros según tu configuración)
conexion = pymysql.connect(
    host='localhost',       # Cambia por el host de tu base de datos
    user='root',      # Cambia por tu nombre de usuario
    password='', # Cambia por tu contraseña
    database='empleados_db' # Cambia por el nombre de tu base de datos
)

try:
    # Crea un cursor para ejecutar consultas SQL
    with conexion.cursor() as cursor:
        # Ejecuta una consulta simple para verificar la conexión
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Conexión exitosa. Versión de la base de datos: {version[0]}")
finally:
    # Cierra la conexión
    conexion.close()
