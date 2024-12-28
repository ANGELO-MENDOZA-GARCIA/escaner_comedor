from db_utils import conectar_bd
from scanner_utils import leer_codigo_barras
from registro_utils import registrar_acceso
from scheduler_utils import iniciar_scheduler
import threading

def main():
    print("Bienvenido al sistema de control de acceso al comedor")
    host = input("Host de la base de datos: ")
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    bd = input("Nombre de la base de datos: ")
    puerto = int(input("Puerto: "))

    conexion = conectar_bd(host, usuario, password, bd, puerto)
    if not conexion:
        print("No se pudo conectar a la base de datos. Saliendo...")
        return

    # Iniciar el scheduler en un hilo aparte
    scheduler_thread = threading.Thread(target=iniciar_scheduler, args=(conexion,))
    scheduler_thread.daemon = True
    scheduler_thread.start()

    puerto_usb = input("Ingrese el puerto del escáner: ")
    while True:
        codigo = leer_codigo_barras(puerto_usb)
        print("Código escaneado:", codigo)
        mensaje = registrar_acceso(conexion, codigo)
        print(mensaje)

if __name__ == "__main__":
    main()
