from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import requests

app = Flask(__name__)

# Sua chave secreta do reCAPTCHA
RECAPTCHA_SECRET_KEY = 'SUA_CHAVE_SECRETA'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')


@app.route('/roupas')
def roupas():
    connection = get_database_connection()
    if connection is None:
        return "Error connecting to database", 500

    cursor = connection.cursor(dictionary=True)

    # Fetch data from CLIENTE table
    cursor.execute("SELECT * FROM CLIENTE")
    clientes = cursor.fetchall()

    # Fetch data from PRODUTO table
    cursor.execute("SELECT * FROM PRODUTO")
    produtos = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('index.html', clientes=clientes, produtos=produtos)


def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root753",
            database="ecomerce"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True)
