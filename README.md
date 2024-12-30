# Gestión de Colaboradores y Escáner de Códigos de Barras

Este repositorio contiene una serie de proyectos que evolucionan desde una conexión básica a bases de datos MySQL hasta un sistema avanzado de gestión de colaboradores con integración de escaneo de códigos de barras.  

## Contenido del Repositorio

### 1. **Intento 3/conexion.py**
   - **Descripción:** Código inicial que establece una conexión básica a una base de datos MySQL y lista las bases de datos disponibles.
   - **Tecnologías utilizadas:**
     - Python
     - MySQL Connector
   - **Funcionalidad principal:** Comprueba la conexión a un servidor MySQL y muestra las bases de datos accesibles.

### 2. **Intento 4/base3.py**
   - **Descripción:** Una aplicación GUI desarrollada con Tkinter para gestionar registros en una base de datos MySQL.  
   - **Tecnologías utilizadas:**
     - Python
     - Tkinter
     - MySQL Connector
   - **Funciones principales:**
     - Insertar, editar, buscar y eliminar registros.
     - Interfaz gráfica sencilla y funcional.
   - **Aplicación:** Ideal para aprender a integrar Python con bases de datos y diseñar formularios básicos.

### 3. **Lector de código de barras/main.py**
   - **Descripción:** Implementación de un sistema de captura de códigos de barras con escucha en segundo plano.  
   - **Tecnologías utilizadas:**
     - Python
     - Tkinter
     - Pynput
   - **Funcionalidad principal:** 
     - Captura de códigos de barras ingresados desde un escáner.
     - Visualización en tiempo real en la interfaz gráfica.

### 4. **Resultado final/main.py**
   - **Descripción:** Una aplicación avanzada que combina la funcionalidad de gestión de registros con el escaneo de códigos de barras.  
   - **Tecnologías utilizadas:**
     - Python
     - Tkinter
     - MySQL Connector
     - Pynput
   - **Funciones principales:**
     - Búsqueda automática de datos de colaboradores en la base de datos al escanear su código.
     - Gestión completa de registros (insertar, editar, buscar, eliminar).
     - Interfaz gráfica optimizada para su uso en sistemas de gestión.

---

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior.
- MySQL instalado y configurado.
- Dependencias Python: 
  ```bash
  pip install mysql-connector-python pynput
  ```

### Configuración de la Base de Datos
1. Crear una base de datos llamada `misdatos`.
2. Crear una tabla con la siguiente estructura:
   ```sql
   CREATE TABLE misdatos (
       id INT PRIMARY KEY,
       nombres VARCHAR(50),
       apellidos VARCHAR(50),
       telefono VARCHAR(15),
       email VARCHAR(50),
       numero_colaborador VARCHAR(20)
   );
   ```

### Ejecución
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ANGELO-MENDOZA-GARCIA/escaner_comedor
   ```
2. Navegar al directorio del archivo deseado.
3. Ejecutar el archivo Python correspondiente:
   ```bash
   python main.py
   ```

---

## Uso

### Para el programa de gestión:
- Ingresar los datos en los campos y usar los botones para realizar acciones (insertar, buscar, editar, eliminar, limpiar).

### Para el lector de códigos de barras:
- Escanear un código y automáticamente se buscará en la base de datos. Si el colaborador existe, los datos se mostrarán en la interfaz.

---

## Contribuciones
¡Contribuciones son bienvenidas! Por favor, abre un *issue* o envía un *pull request* con tus sugerencias.

---

## Autor
Desarrollado por Angelo(https://github.com/ANGELO-MENDOZA-GARCIA).

--- 

Este `README.md` explica el propósito, uso y configuración del repositorio, además de resaltar su evolución, desde conceptos básicos hasta aplicaciones más avanzadas. 
