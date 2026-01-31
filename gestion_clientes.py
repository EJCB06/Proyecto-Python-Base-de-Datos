import mysql.connector
from mysql.connector import Error

# Función para conectar con la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='javier',  # o 'edwin'
            password='Admin1234',
            database='GestionClientes'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Función para ver todos los clientes
def ver_clientes():
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()
            print("\n--- Lista de Clientes ---")
            for fila in resultados:
                print(f"ID: {fila[0]}, Nombre: {fila[1]}, Teléfono: {fila[2]}, Email: {fila[3]}")
        except Error as e:
            print(f"Error al obtener los datos: {e}")
        finally:
            conexion.close()

# Función para insertar un nuevo cliente
def insertar_cliente():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "INSERT INTO clientes (nombre, telefono, email) VALUES (%s, %s, %s)"
            datos = (nombre, telefono, email)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Cliente insertado correctamente.")
        except Error as e:
            print(f"Error al insertar: {e}")
        finally:
            conexion.close()

# Función para modificar un cliente existente
def modificar_cliente():
    try:
        id_cliente = int(input("ID del cliente a modificar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_telefono = input("Nuevo teléfono: ")
        nuevo_email = input("Nuevo email: ")
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            consulta = "UPDATE clientes SET nombre = %s, telefono = %s, email = %s WHERE id = %s"
            datos = (nuevo_nombre, nuevo_telefono, nuevo_email, id_cliente)
            cursor.execute(consulta, datos)
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró un cliente con ese ID.")
            else:
                print("Cliente actualizado correctamente.")
    except ValueError:
        print("ID inválido. Debe ser un número.")
    except Error as e:
        print(f"Error al modificar: {e}")
    finally:
        if 'conexion' in locals() and conexion:
            conexion.close()

# Función para borrar un cliente
def borrar_cliente():
    try:
        id_cliente = int(input("ID del cliente a borrar: "))
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            consulta = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(consulta, (id_cliente,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró un cliente con ese ID.")
            else:
                print("Cliente eliminado correctamente.")
    except ValueError:
        print("ID inválido. Debe ser un número.")
    except Error as e:
        print(f"Error al borrar: {e}")
    finally:
        if 'conexion' in locals() and conexion:
            conexion.close()

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Ver clientes")
        print("2. Insertar cliente")
        print("3. Modificar cliente")
        print("4. Borrar cliente")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ver_clientes()
        elif opcion == '2':
            insertar_cliente()
        elif opcion == '3':
            modificar_cliente()
        elif opcion == '4':
            borrar_cliente()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
