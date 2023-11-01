#Habilitamos el modulo de flask para la ejecucion de la app e importamos la informacion de sqlite3
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
#Habilitamos flask
app = Flask(__name__)
#Generamos unafuncion para realizar un select a los productos de la tabla menu de la base de datos
def get_products():
    with sqlite3.connect('Burger_CMS.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Menu")
        products = cursor.fetchall()
    return products
#generamos el app rute para la primera pagina de nuestra app donde solicitaremos que se ingrese un id de cliente
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        client_id = request.form.get('client_id')
        return redirect(url_for('order', client_id=client_id))
    return render_template('index.html')
#generamos el app route donde el usuario realizara su orden de los productos 
@app.route('/order/<client_id>', methods=['GET', 'POST'])
def order(client_id):
    products = get_products()
    if request.method == 'POST':
        selected_products = request.form.getlist('product')
        total_price = sum([float(p.split('|')[1]) for p in selected_products])
        #Al realizar el pedido se Genera ticket con los datos del pedido
        with open('ticket.txt', 'w') as f:
            f.write('Productos seleccionados:\n')
            for product in selected_products:
                f.write(product.split('|')[0] + '\n')
            f.write(f'Total a pagar: ${total_price}')
        return render_template('done.html', total_price=total_price)
    return render_template('order.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)