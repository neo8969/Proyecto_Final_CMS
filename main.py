#Exportamos las funciones de los archivos de clientes, menu y pedidos
from clientes import Clientes
from menu import *          
from pedido import *      
#Creamos la funcion de imprimir_ticket haciendo una consulta directa al archivo de pedidos 
def imprimir_ticket(pedido_id):
    pedido_data = pedidos.pedidos[pedido_id]
    print("\n---- TICKET ----")
    print(f"Pedido ID: {pedido_id}")
    print(f"Cliente: {pedido_data['cliente']}")
    print(f"Producto: {pedido_data['producto']}")
    print(f"Precio: ${pedido_data['precio']}")
    print("-----------------\n")
#Colocamos las funciones que queremos consumir de los archivos
clientes = Clientes()
menu = Menu()
pedidos = Pedido()
#Colocamos una condicional while donde seleccionamos que una opcion
while True:
    print("Seleccione una opción:")
    print("1. Agregar Cliente")
    print("2. Agregar Producto al Menú")
    print("3. Hacer un Pedido")
    print("4. Consultar Pedido")
    print("5. Cancelar Pedido")
    print("6. Salir")
    
    opcion = input("Opción: ")
#Colocamos un if en caso de seleccionar la opcion 1 la cual nos dara la opcion de ingresar un nuevo cliente
    if opcion == '1':
        clave = input("Ingrese clave de cliente: ")
        nombre = input("Ingrese nombre de cliente: ")
        direccion = input("Ingrese dirección: ")
        correo = input("Ingrese correo electrónico: ")
        telefono = input("Ingrese teléfono: ")
        clientes.agregar(clave, nombre, direccion, correo, telefono)
#Colocamos un elif en caso de seleccionar la opcion 2 la cual nos dara la opcion de ingresar un nuevo producto a menu        
    elif opcion == '2':
        clave = input("Ingrese clave de producto: ")
        nombre = input("Ingrese nombre de producto: ")
        precio = float(input("Ingrese precio: "))
        menu.agregar(clave, nombre, precio)
#Colocamos un elif en caso de seleccionar la opcion 3 la cual nos dara la opcion de ingresar un un pedido       
    elif opcion == '3':
        pedido_id = int(input("Ingrese ID de pedido: "))
        cliente = input("Ingrese clave de cliente: ")
        producto = input("Ingrese clave de producto: ")
        precio = float(input("Ingrese precio: "))
        pedidos.crear_pedido(pedido_id, cliente, producto, precio)
#colocamos un elif para la opcion 4 esta nos permitira realizar una consulta a los pedidos         
    elif opcion == '4':
        pedido_id = int(input("Ingrese ID de pedido para consultar: "))
        if pedido_id in pedidos.pedidos:
            imprimir_ticket(pedido_id)
        else:
            print("Pedido no encontrado.")
#Colocamos un elif para la opcion 5 la cual nos dara una opcion para cancelar los pedidos             
    elif opcion == '5':
        pedido_id = int(input("Ingrese ID de pedido para cancelar: "))
        pedidos.cancelar_pedido(pedido_id)
#Colocamos un elif para la opcion 6 con la opcion de salir para salir del menu        
    elif opcion == '6':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
#Cerramos conexiones con las funciones
clientes.cerrar_conexion()
menu.cerrar_conexion()
pedidos.cerrar_conexion()
