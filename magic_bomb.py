from binance.client import Client
from binance.websockets import BinanceSocketManager
# import binance.expections
# from json2table import convert
import json

class magic_bomb:
    def __init__(self,api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        try: 
            self.client = Client(self.api_key, self.api_secret)
            print("Client authenticated")
        except BinanceAPIException as e:
            print(e.status_code)
            print(e.message)
    def account(self):
        account = self.client.get_account()
        for value in account['balances']:
            if (float(value['free']) != float(0)) or (float(value['locked']) != float(0)):
                print(value)
