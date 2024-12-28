import schedule
import time

def borrar_registros_diarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM accesos")
    conexion.commit()
    print("Registros limpiados.")

# Programar tarea diaria
schedule.every().day.at("00:00").do(borrar_registros_diarios, conexion)

while True:
    schedule.run_pending()
    time.sleep(1)
