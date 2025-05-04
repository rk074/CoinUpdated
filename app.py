from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz
from fetcher.fetchCoinPrice import CoinDCXAPI

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/coinprice')
def get_coin_details():
    coin_data = CoinDCXAPI()
    coin_price_data = coin_data.get_coin_details(['BTCUSDT', 'DOGEUSDT', 'PEPEUSDT'])
    required_fields = ['market', 'last_price']
    # coin_price_data = coin_data.get_binance_coin_data(['BTCUSDT', 'DOGEUSDT', '1000PEPEUSDT'])
    # required_fields = ['symbol', 'price']
    print(coin_price_data)
    if coin_price_data:
        coin_price_data_list = [[coin_price.get(field) for field in required_fields] for coin_price in coin_price_data]
    else:
        coin_price_data_list = []

    print(coin_price_data_list)
    return jsonify(coin_price_data_list)


if __name__ == '__main__':
    app.run(debug=True)
