from magic_bomb import magic_bomb
from magic_bomb import websocket
from binance.client import Client
api_key=""
api_secret=""
binance = magic_bomb(api_key, api_secret)

# account = binance.account()

# pair = binance.pairs()

# print(binance.get_istorical_trades())
# print(binance.get_balance_pair('CHZUSDT'))
binance.get_coins()
# print(binance.total_balance())


# websocket = websocket(api_key, api_secret)
# websocket = websocket.websocket()
