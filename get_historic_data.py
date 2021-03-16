from magic_bomb import magic_bomb
from magic_bomb import websocket
from binance.client import Client
from pprint import pprint
from datetime import datetime
import matplotlib.pyplot as plt

api_key=""
api_secret=""
binance = magic_bomb(api_key, api_secret)

klines = binance.get_historical_klines('CHZUSDT','5 days ago UTC')
# pprint(klines)
# for kline in klines['high']:
#     print('high {}'.format(kline))
max_klines = max(klines, key=lambda ev: ev['high'])
min_klines = min(klines, key=lambda ev: ev['low'])
avg_max = max(klines, key=lambda ev: ev['avg'])
avg_min = min(klines, key=lambda ev: ev['avg'])
pprint(klines)
pprint(klines)
print(avg_max)
print(avg_min)
print('max: {}, min: {}, avg_max: {}, avg_min: {}'.format(max_klines['high'],min_klines['low'],avg_max['avg'],avg_min['avg']))
# plt.plot(klines['date'], klines['high'])
