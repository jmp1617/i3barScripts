#!/usr/bin/env python3

import requests

mine = requests.get(url="https://ethermine.org/api/miner_new/B0b359582fEb5973178D0c6CfBBE59474c69e207").json()
stats = requests.get(url="https://api.ethermine.org/poolStats").json()

current = stats['data']['price']['usd']
hashrate = mine['workers']['glados']['hashrate']
unpaid = int(str(mine['unpaid']))/1000000000000000000
balance = float(current)*float(unpaid)

#print(hashrate,unpaid,current,"")
print(hashrate,round(unpaid,5),"$"+format(round(balance,2),'.2f'),"")
