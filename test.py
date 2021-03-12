from magic_bomb import magic_bomb
from binance.client import Client
api_key="AY5bm2HEn6w5OUAAhCQzt1Ifrwl5EnLGKRAJAf9ZTpLsQfc18KrAQMCxobiQYH5y"
api_secret="cZREtIOeWVYCo3Jsa8kgMRBMiRlVsdigawMklBB5fFKkGuU04xZjFwdyFkoxWKF3"
binance = magic_bomb(api_key, api_secret)

# account = binance.account()

pair = binance.pairs()
