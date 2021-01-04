from binance.client import Client
import time

api_key = '----API KEY-------'
api_secret = '-------SECRET KEY----------'

client = Client(api_key, api_secret)


mycoin = ['BTCUSDS','DOGEBUSD','ETHBUSD']
mycoin = ['ETHBUSD']

while True:
    prices = client.get_all_tickers()    
    for p in prices:
        for c in mycoin :
            sym = c
            if p['symbol'] == sym :
                print(p)
                pc = float(p['price'])
                rate = 30.01
                cal = pc * rate
                print('เหรียญ {} ราคา {}'.format(sym,cal))
                print('ราคา usd {}'.format(pc))
                print('------------')
    time.sleep(0.2)
