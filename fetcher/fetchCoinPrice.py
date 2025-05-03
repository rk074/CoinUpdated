import requests


class CoinDCXAPI:
    market_data_url = "https://api.coindcx.com/exchange/ticker"

    def __init__(self):
        pass

    @staticmethod
    def __fetch_api_url(api_url, params=None):
        # Making a GET request to the API
        response = requests.get(api_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            return data
        else:
            print(f"Error: {response.status_code}")
            return None

    def __get_required_coin_details(self):
        required_fields = ['market', 'last_price', 'change_24_hour']
        coin_data = self.__fetch_api_url(self.market_data_url)
        coin_price_details = {}
        if coin_data:
            for dict_data in coin_data:
                req_dict = {key: dict_data.get(key, '') for key in required_fields}
                try:
                    lst_price = float(req_dict['last_price'])
                    lst_price = round(lst_price, 2) if lst_price > 10 else lst_price
                    req_dict['last_price'] = lst_price
                except:
                    pass
                coin_name = dict_data.get('market')
                if coin_name:
                    coin_price_details[coin_name] = req_dict
            return coin_price_details
        return None

    def get_coin_details(self, coin_names):
        coin_price_details = self.__get_required_coin_details()
        if coin_price_details:
            if isinstance(coin_names, list):
                res_list = [coin_price_details.get(coin_name) for coin_name in coin_names]
                return res_list
            else:
                return coin_price_details.get(coin_names)
        return None


if __name__ == '__main__':
    obj = CoinDCXAPI()
    print(obj.get_coin_details('BTCUSDT'))
