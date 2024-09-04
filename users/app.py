from flask import Flask, render_template, redirect, url_for
import requests
from data import users

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/user/<int:user_id>')
def user_orders(user_id):
    return redirect(f'http://localhost:5001/orders/{user_id}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)