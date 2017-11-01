#!/usr/bin/env python3

import requests
btc = requests.get(url='https://api.coindesk.com/v1/bpi/currentprice/usd.json').json()['bpi']['USD']['rate'].split('.')[0]
eth = requests.get(url="https://api.ethermine.org/poolStats").json()['data']['price']['usd']

print(btc,"e",eth,"")
