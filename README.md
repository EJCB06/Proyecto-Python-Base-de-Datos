# Proyecto: Gestión de BD con Python y MySQL

**Módulo:** Administración de Sistemas Informáticos en Red / Programación  
**Autores:** Edwin Javier Cueva Berenguer y Javier Sánchez López  
**Curso:** 2025/2026  
**Centro:** IES Celia Viñas


## Tecnologías Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)



## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación de consola (CLI) en **Python** para la gestión de una base de datos **MySQL**. El objetivo principal es demostrar la integración entre un lenguaje de programación de alto nivel y un sistema gestor de bases de datos relacional, implementando operaciones CRUD (Create, Read, Update, Delete) de forma segura y eficiente.



## Memoria Técnica: Implementación y Entorno

Para el desarrollo de la aplicación, hemos seguido un procedimiento estructurado en cinco etapas fundamentales, partiendo de la premisa de que disponemos de un servidor MySQL activo en nuestro *host*.

### 1. Inicialización y Creación de la Base de Datos
El primer paso consiste en establecer la conexión con el servidor de bases de datos a través de la interfaz de línea de comandos (CLI). Para garantizar la seguridad y trazabilidad, evitamos el uso del usuario `root`, accediendo en su lugar con nuestras credenciales de usuario específicas mediante el flag `-u` para el usuario y `-p` para solicitar la autenticación por contraseña.

Una vez dentro del monitor de MySQL, procedemos a definir el contenedor de nuestros datos mediante una sentencia DDL (*Data Definition Language*):

```SQL
# Acceso al sistema gestor de base de datos
mysql -u [usuario] -p
-- Creación del esquema lógico
CREATE DATABASE GestionClientes;
```

![🖼️ INSERTAR IMAGEN nº1 AQUÍ: Captura de pantalla de la terminal mostrando el comando CREATE DATABASE y el mensaje "Query OK"](images/1.png)



### 2. Modelado de Datos: Estructura de la Tabla
Diseñamos la tabla clientes estableciendo una estructura relacional lógica. Definimos el campo id como clave primaria (PRIMARY KEY) y autoincremental para asegurar la unicidad. Para los campos de información (nombre, telefono, email), utilizamos VARCHAR con longitudes limitadas.

```SQL
USE GestionClientes;

-- Definición de la estructura de la tabla (Schema)
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único
    nombre VARCHAR(50),                
    telefono VARCHAR(20),
    email VARCHAR(50)
);
```

![🖼️ INSERTAR IMAGEN nº2 AQUÍ: Captura mostrando la creación de la tabla y/o un DESCRIBE clientes;](images/2.png)

### 3. Poblado de Datos (Mock Data)
Antes de programar en Python, verificamos la estructura de la BD mediante una inserción manual de datos de prueba (sentencias DML). Esto nos permite tener registros visibles al conectar la aplicación por primera vez.

```SQL
-- Inserción de registros iniciales
INSERT INTO clientes (nombre, telefono, email)
VALUES
('Ana López', '600123123', 'ana@example.com'),
('Carlos Ruiz', '611222333', 'carlos@example.com');
```


![🖼️ INSERTAR IMAGEN nº3 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/3.png)

```SQL
-- Verificación de la integridad de los datos
SELECT * FROM clientes;
```

![🖼️ INSERTAR IMAGEN nº4 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/4.png)

### 4. Gestión de Dependencias
Para vincular Python con MySQL, es necesario instalar un driver. Python no incluye esta funcionalidad en su biblioteca estándar, por lo que recurrimos a pip para instalar el conector oficial.

Comandos ejecutados en la VM Ubuntu:

```Bash
# Actualización e instalación de pip
sudo apt install python3-pip

# Instalación del driver oficial
pip3 install mysql-connector-python
```

![🖼️ INSERTAR IMAGEN nº5 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/5.png)


```Bash
# Verificación de la instalación: Ejecutamos un pequeño script en línea para confirmar que el módulo se carga correctamente:

python3 -c "import mysql.connector; print('OK - Librería cargada correctamente')"
```

![🖼️ INSERTAR IMAGEN nº6 AQUÍ: Captura de la instalación con pip (donde se vea "Successfully installed") y el test de importación](images/6.png)


### 5. Organización del Espacio de Trabajo
Preparamos el entorno de desarrollo local creando un directorio específico para mantener el proyecto modular.

```Bash
mkdir ~/gestion_clientes
cd ~/gestion_clientes
```

![🖼️ INSERTAR IMAGEN nº7 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/7.png)

```Bash
nano gestion_clientes.py
# El archivo gestion_clientes.py contendrá la lógica principal del programa, incluyendo el menú interactivo y el manejo de excepciones.
```

![🖼️ INSERTAR IMAGEN nº8 AQUÍ: Captura del explorador de archivos o terminal mostrando la carpeta creada](images/8.png)


## ¿Cómo Ejecutar el Proyecto?
**Primero** tendremos que Clonar este repositorio:

```Bash
git clone https://github.com/usuario/repo.git

# Instalar dependencias:

pip3 install mysql-connector-python
# Ejecutar el script:

python3 gestion_clientes.py
```

## Comprobaciones

![🖼️ INSERTAR IMAGEN nº9 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/9.png)

Conforme iniciemos nos encontraremos con el siguiente menú en nuestra consola (lo más bonito que se podía hacer mediante CLI)

![🖼️ INSERTAR IMAGEN nº11 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/11.png)

La primera opción es para ver a los clientes que tenemos creados en nuestra base de datos de MySQL.

![🖼️ INSERTAR IMAGEN nº10 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/10.png)

La segunda opción podemos ver como hemos insertado a nuestro usuario *FedeLobo* en nuestra base de datos y le hemos adjuntado el contenido que necesitabamos para la creación de un nuevo usuario en la base de datos.


![🖼️ INSERTAR IMAGEN nº12 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/final.png)

Y aquí podemos ver como funciona la ejecución de borrar un usuario de la base de datos. 


![🖼️ INSERTAR IMAGEN nº12 AQUÍ: Captura del SELECT * FROM clientes mostrando los datos introducidos](images/12.png)

Por último podemos ver como nos podemos salir del programa sin ningún tipo de pega.

IES Celia Viñas - Proyecto de Programación 2025/2026
