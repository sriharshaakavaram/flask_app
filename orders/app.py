from flask import Flask, render_template, redirect, url_for
from data import orders

app = Flask(__name__)

@app.route('/orders/<int:user_id>')
def user_orders(user_id):
    user_orders = orders.get(user_id, [])
    return render_template('orders.html', orders=user_orders)

@app.route('/order/<int:order_id>')
def order_items(order_id):
    return redirect(f'http://localhost:5002/items/{order_id}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)