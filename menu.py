#Se importa la informacion de sqlite3
import sqlite3
#Creamos la clase Menu
class Menu:
#Creamos la funcion para comunicar con la base de datos Burger CMS
    def __init__(self):
        self.conexion = sqlite3.connect('Burger_CMS.db')
        self.cursor = self.conexion.cursor()
#Creamos la funcion que nos permitira agregar productos a la tabla menu
    def agregar(self, clave, nombre, precio):
        try:
            self.cursor.execute('''
            INSERT INTO Menu (clave, nombre, precio) 
            VALUES (?, ?, ?)
            ''', (clave, nombre, precio))
            self.conexion.commit()
            print(f"Producto {nombre} agregado exitosamente al menú.")
        except sqlite3.Error as e:
            print(f"Error al agregar el producto al menú: {e}")
#Creamos la funcion para actualizar datos de la tabla menu
    def actualizar(self, clave, nombre=None, precio=None):
        try:
            if nombre:
                self.cursor.execute("UPDATE Menu SET nombre = ? WHERE clave = ?", (nombre, clave))
            if precio is not None:
                self.cursor.execute("UPDATE Menu SET precio = ? WHERE clave = ?", (precio, clave))

            self.conexion.commit()
            print(f"Producto con clave {clave} actualizado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar el producto: {e}")
#Creamos la funcion para elmininar productos en la tabla de menu
    def eliminar(self, clave):
        try:
            self.cursor.execute("DELETE FROM Menu WHERE clave = ?", (clave,))
            self.conexion.commit()
            print(f"Producto con clave {clave} eliminado exitosamente del menú.")
        except sqlite3.Error as e:
            print(f"Error al eliminar el producto: {e}")
#Cerramo la conexion a la base
    def cerrar_conexion(self):
        self.conexion.close()


#Llamamos a la clase Menu del archivo menu
menu = Menu()

# Esta opcion nos servidra para ingresar producto al menú de manera manual
menu.agregar('5', 'Galleta', 10.00)

#Esta opcion esta comentada ya que la habilitaremos si deseamos actualizar algun producto
#menu.actualizar('1', nombre='Hamburguesa', precio=70.00)

#Esta opcion esta comentada ya que la habilitaremos si deseamos eliminar algun producto del menú
#menu.eliminar('1')

#Cerramos conexion
menu.cerrar_conexion()
