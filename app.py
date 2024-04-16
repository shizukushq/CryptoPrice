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

# Основной маршрут для отображения главной страницы
@app.route('/')
def index():
    return render_template('index.html', price=round(get_ton_price(), 2))

# Маршрут для получения цены криптовалюты TON в формате JSON
@app.route('/get_price')
def get_price():
    price = round(get_ton_price(), 2)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run()
