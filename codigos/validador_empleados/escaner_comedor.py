import mysql.connector
from mysql.connector import Error
import tabulate

def conectar_a_base_datos():
    try:
        # Configuración de la conexión
        conexion = mysql.connector.connect(
            host='tu-servidor-en-linea.com',  # Dirección del servidor
            user='tu-usuario',               # Usuario de la base de datos
            password='tu-contraseña',        # Contraseña del usuario
            database='nombre_de_tu_base'     # Nombre de la base de datos
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
