import requests
import json 

url = "https://nbu.uz/en/exchange-rates/json/"

def send_req(url):
    base = requests.get(url)
    return base 

def makeJson(base):
    madeJSON = json.loads(base.content)
    return madeJSON 

def get_uzbeksum(data: list):
    calc = data[-1]
    summa = calc['nbu_buy_price']
    dollar = int(input("Dollar kirizing: "))
    
    calculator = float(summa)*dollar
    return calculator

requested_data = send_req(url)
makeJS = makeJson(requested_data)
summa = get_uzbeksum(makeJS)

def hellofunc():
    return "Hello function"

print(summa)
