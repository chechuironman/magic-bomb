from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.websockets import BinanceSocketManager

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
        # for value in account['balances']:
            # if (float(value['free']) != float(0)) or (float(value['locked']) != float(0)):
            #     print(value)
        print(account)
    # def get_pairs(self):
    def get_istorical_trades(self):
        trades = self.client.get_historical_trades(symbol='CHZBUSD')  
        print(trades)  
    def get_all_orders(self, pair):
        orders = self.client.get_all_orders(symbol=pair) 
        success_orders=[]
        for order in orders:
            if order['status'] != 'CANCELED':
                success_orders.append(order)
        return success_orders 
    def get_balance_pair(self, pair):
        orders = self.get_all_orders( pair)
        BUYS=0
        SELLS=0
        for order in orders:
            if order['side'] == 'SELL':
                SELLS = SELLS + (float(order['executedQty'])*float(order['price']))
            else:
                if order['side'] == 'BUY':
                    BUYS = BUYS + (float(order['executedQty'])*float(order['price']))
                else: 
                    print("hay mas mierda")      
        balance = SELLS - BUYS
        return balance
    def get_coins(self):
        details = self.client.get_all_tickers()
        coins = []
        for coin in details:
            coins.append(coin['symbol'])
        print(coins)

    # def get_all_coins(self):
    #     coins = self.client.get_all_coins_info()
    #     print(coins)
    # def margin_trades(self):
    #     trades = self.client.get_margin_trades(symbol='CHZUSDT')
    #     print(trades)

class websocket:   
    def __init__(self,api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        try: 
            self.client = Client(self.api_key, self.api_secret)
            print("Client authenticated")
        except BinanceAPIException as e:
            print(e.status_code)
            print(e.message) 
    def websocket(self):
        bm = BinanceSocketManager(self.client)
        # start any sockets here, i.e a trade socket
        conn_key = bm.start_trade_socket('BNBBTC', self.process_message)
        # then start the socket manager
        bm.start()  
    def process_message(self, msg):
        print("message type: {}".format(msg['e']))
        print(msg)
    # do something    
