import serial

def leer_codigo_barras(puerto):
    with serial.Serial(puerto, 9600, timeout=1) as scanner:
        codigo = scanner.readline().decode('utf-8').strip()
        return codigo
