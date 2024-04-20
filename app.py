from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# ключ API CoinGecko
API_KEY = "CG-J4WVeSaak94SUY4dcN35d6Rd"

# Функция для получения цены TON
def get_ton_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {
        'x-cg-demo-api-key': API_KEY,
    }
    params = {
        'ids': 'the-open-network',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, headers=headers, params=params).json()
    return response['the-open-network']['usd']

# Функция для получения цены Bitcoin
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {
        'x-cg-demo-api-key': API_KEY,
    }
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, headers=headers, params=params).json()
    return response['bitcoin']['usd']

def get_ethereum_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {
        'x-cg-demo-api-key': API_KEY,
    }
    params = {
        'ids': 'ethereum',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, headers=headers, params=params).json()
    return response['ethereum']['usd']

# Основной маршрут для отображения главной страницы
@app.route('/')
def TON():
    return render_template('TON.html', ton_price=round(get_ton_price(), 2))

# # Основной маршрут для отображения страницы с курсом TON
# @app.route('/ton')
# def TON():
#     return render_template('TON.html', ton_price=round(get_ton_price(), 2))

# Основной маршрут для отображения страницы с курсом Bitcoin
@app.route('/bitcoin')
def BIT():
    return render_template('BIT.html', bit_price=round(get_bitcoin_price(), 2))

# Основной маршрут для отображения страницы с курсом Ethereum
@app.route('/ethereum')
def ETH():
    return render_template('ETH.html', eth_price=round(get_ethereum_price(), 2))

# Маршрут для получения цены криптовалюты TON в формате JSON
@app.route('/ton_price')
def ton_price():
    price = round(get_ton_price(), 2)
    return jsonify({'the-open-network': price})

# Маршрут для получения цены криптовалюты Bitcoin в формате JSON
@app.route('/bit_price')
def bit_price():
    price = round(get_bitcoin_price(), 2)
    return jsonify({'bitcoin': price})

# Маршрут для получения цены криптовалюты Ethereum в формате JSON
@app.route('/eth_price')
def eth_price():
    price = round(get_ethereum_price(), 2)
    return jsonify({'ethereum': price})

if __name__ == '__main__':
    app.run()
