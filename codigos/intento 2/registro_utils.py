from datetime import date

def registrar_acceso(conexion, id_empleado):
    cursor = conexion.cursor()
    hoy = date.today()

    # Verificar si el empleado ya ingresó hoy
    cursor.execute(
        "SELECT * FROM accesos WHERE empleado_id = %s AND fecha = %s",
        (id_empleado, hoy)
    )
    if cursor.fetchone():
        return "Acceso denegado: ya registrado hoy."

    # Registrar entrada
    cursor.execute(
        "INSERT INTO accesos (empleado_id, fecha) VALUES (%s, %s)",
        (id_empleado, hoy)
    )
    conexion.commit()
    return "Acceso registrado correctamente."
