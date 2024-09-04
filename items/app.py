from flask import Flask, render_template
from data import items

app = Flask(__name__)

@app.route('/items/<int:order_id>')
def order_items(order_id):
    order_items = items.get(order_id, [])
    return render_template('items.html', items=order_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)