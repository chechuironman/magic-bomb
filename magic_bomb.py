from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.websockets import BinanceSocketManager
from datetime import datetime
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
        all_values = []
        account_values = []
        for value in account['balances']:
            if (float(value['free']) != float(0)) or (float(value['locked']) != float(0)):
                account_values.append(value)
            all_values.append(value['asset'])
        # return json.dumps({"all_values": all_values,"count_values": account_values})
        return all_values
    # def get_pairs(self):
    def get_historical_trades(self):
        trades = self.client.get_historical_trades(symbol='CHZBUSD')  
        print(trades)  
    def get_all_orders(self, pair):
        orders = self.client.get_all_orders(symbol=pair) 
        success_orders=[]
        for order in orders:
            if order['status'] != 'CANCELED':
                success_orders.append(order)
        return success_orders 
    def get_balance_pair(self):
        orders = self.get_all_orders('ALL')
        print(orders)
        # BUYS=0
        # SELLS=0
        # for order in orders:
        #     if order['side'] == 'SELL':
        #         SELLS = SELLS + (float(order['executedQty'])*float(order['price']))
        #     else:
        #         if order['side'] == 'BUY':
        #             BUYS = BUYS + (float(order['executedQty'])*float(order['price']))
        #         else: 
        #             print("hay mas mierda")      
        # balance = SELLS - BUYS
        # return balance
    def get_coins(self):
        details = self.client.get_all_tickers()
        coins = []
        for coin in details:
            coins.append(coin['symbol'])
        return coins
    def total_balance(self):
        pairs = self.get_coins()
        # print(pairs)
        # print(values['all_values'])
        # pairs = values['all_values']
        balances = []
        for pair in pairs:
            print('pair: {}', pair)
            balances.append(self.get_balance_pair(pair))
        return balances
    def get_asset_dividend_histrory(self):
        print(self.client.get_asset_dividend_history())
    def get_my_trades(self):
        print(self.client.get_my_trades(symbol=''))
    def get_historical_trades(self,pair):
        trades = self.client.get_historical_trades(symbol=pair)
        return(trades)
    def get_historical_klines(self,pair, period):
        klines = self.client.get_historical_klines(pair, Client.KLINE_INTERVAL_1MINUTE, period)
        clean_klines = []
        for kline in klines:
            clean_klines.append({'date':datetime.fromtimestamp(int(kline[0])/1000), 'high': kline[2], 'low': kline[3], 'avg': (float(kline[2])+float(kline[3]))/2})
        return clean_klines
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
