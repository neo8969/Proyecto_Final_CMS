#Realizamos el import de sqlite3
import sqlite3
#Creamos la clase Pedido
class Pedido:
#Generamos el modulo para comunicar con la informacion de Burger CMS
    def __init__(self):
        self.conexion = sqlite3.connect('Burger_CMS.db')
        self.cursor = self.conexion.cursor()
        self.pedidos = {}
#Creamos la funcion de crear pedido para generar pedidos
    def crear_pedido(self, pedido, cliente, producto, precio):
        if pedido in self.pedidos:
            print(f"El número de pedido {pedido} ya existe.")
            return
#Definimos en donde iran lo datos del pedido
        self.pedidos[pedido] = {
            'cliente': cliente,
            'producto': producto,
            'precio': precio
        }
#Realizamos un insert para que los datos se ingresen en la tabla pedido
        try:
            self.cursor.execute('''
            INSERT INTO Pedido (pedido, cliente, producto, precio) 
            VALUES (?, ?, ?, ?)
            ''', (pedido, cliente, producto, precio))
            self.conexion.commit()
            print(f"Pedido {pedido} creado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al crear el pedido: {e}")
#Creamos la funcion de cancelar pedido 
    def cancelar_pedido(self, pedido):
        if pedido not in self.pedidos:
            print(f"El número de pedido {pedido} no existe.")
            return

        del self.pedidos[pedido]

        try:
            self.cursor.execute("DELETE FROM Pedido WHERE pedido = ?", (pedido,))
            self.conexion.commit()
            print(f"Pedido {pedido} cancelado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al cancelar el pedido: {e}")
#Cerramos la comunicacion 
    def cerrar_conexion(self):
        self.conexion.close()


#Llamamos la funcion pedido de la tabla pedido
pedido = Pedido()

# Esta opcion nos servira para crear pedidos por el usuario manualmente
pedido.crear_pedido(1, '1', '1', 50.00)

#Esta opcion estara comentada para poder cancelar pedidos cuando el usuario lo requiera
#pedido.cancelar_pedido(1)

#Cerramos conexión
pedido.cerrar_conexion()
