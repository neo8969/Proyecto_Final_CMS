#Importamos datos de la base de datos BurgerCMS
import sqlite3
#Generamos la clase Clientes donde definiremos los mudulos y las funciones para agregar modificar y elmininar clientes
class Clientes:
    #Definimos a que base nos vamos a conectar 
    def __init__(self):
        self.conexion = sqlite3.connect('Burger_CMS.db')
        self.cursor = self.conexion.cursor()
    #Creamos la funcion para agregar los datos de un cliente donde agregamos un insert y los parametros que se solicitan
    def agregar(self, clave, nombre, direccion, correo_electronico, telefono):
        try:
            self.cursor.execute('''
            INSERT INTO Clientes (clave, nombre, direccion, correo, telefono) 
            VALUES (?, ?, ?, ?, ?)
            ''', (clave, nombre, direccion, correo_electronico, telefono))
            self.conexion.commit()
            print(f"Cliente {nombre} agregado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al agregar el cliente: {e}")
    #Generamos la funcion donde actualizaremos los datos de un cliente donde en la base de datos lo realizaremos con un UPDATE
    def actualizar(self, clave, nombre=None, direccion=None, correo_electronico=None, telefono=None):
        try:
            if nombre:
                self.cursor.execute("UPDATE Clientes SET nombre = ? WHERE clave = ?", (nombre, clave))
            if direccion:
                self.cursor.execute("UPDATE Clientes SET direccion = ? WHERE clave = ?", (direccion, clave))
            if correo_electronico:
                self.cursor.execute("UPDATE Clientes SET correo = ? WHERE clave = ?", (correo_electronico, clave))
            if telefono:
                self.cursor.execute("UPDATE Clientes SET telefono = ? WHERE clave = ?", (telefono, clave))
            #Hacemos el commit para que los datos se ingresen en la tabla 
            self.conexion.commit()
            print(f"Cliente con clave {clave} actualizado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar el cliente: {e}")
    #Generamos la funcion de eliminar donde primero solicitamos la clave del usuario para eliminar el registro
    def eliminar(self, clave):
        try:
            self.cursor.execute("DELETE FROM Clientes WHERE clave = ?", (clave,))
            self.conexion.commit()
            print(f"Cliente con clave {clave} eliminado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al eliminar el cliente: {e}")
    #cerramos la conexion con la base de datos 
    def cerrar_conexion(self):
        self.conexion.close()


# Aqui llamamos del archivo clientes a la clase CLientes que es la que contendra las funciones que desemos ocupar
clientes = Clientes()

# Aqui agregaremos un nuevo cleinte donde colocaremos los datos del mismo
clientes.agregar('4', 'Suei Chong', 'Calle 694', 'suei@email.com', '656545489')

# Esta parate estara comentada a menos que queramos actualizar los datos de un cliente
#clientes.actualizar('1', nombre='Christian Martinez')

# Esta parte estara comentada a menos que queramos eliminar un cliente
#clientes.eliminar('1')

# Cerramos conexión con la base de datos
clientes.cerrar_conexion()