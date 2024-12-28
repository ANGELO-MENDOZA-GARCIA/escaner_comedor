import mysql.connector
from mysql.connector import Error

def conectar_a_base_datos():
    try:
        # Configuración de la conexión
        conexion = mysql.connector.connect(
            host='127.0.0.1',  # Dirección del servidor
            user='root',               # Usuario de la base de datos
            password='',        # Contraseña del usuario
            database='sys'     # Nombre de la base de datos
        )
        
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            # Obtenemos información del servidor
            info_servidor = conexion.get_server_info()
            print("Versión del servidor MySQL:", info_servidor)
            return conexion

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

    finally:
        # Cerramos la conexión después del uso (si no se devuelve como objeto)
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")

# Llamamos a la función
conexion = conectar_a_base_datos()
