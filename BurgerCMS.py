import sqlite3

# Crear la conexión y el cursor
conexion = sqlite3.connect('Burger_CMS.db')
cursor = conexion.cursor()

# Tabla de Clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    clave INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    correo TEXT NOT NULL,
    telefono TEXT NOT NULL
)
''')

# Tabla de Menú
cursor.execute('''
CREATE TABLE IF NOT EXISTS Menu (
    clave INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
''')

# Tabla de Pedido
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedido (
    pedido INTEGER PRIMARY KEY,
    cliente INTEGER NOT NULL,
    producto INTEGER NOT NULL,
    precio REAL NOT NULL,
    FOREIGN KEY (cliente) REFERENCES Clientes(clave),
    FOREIGN KEY (producto) REFERENCES Menu(clave)
)
''')

# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()

