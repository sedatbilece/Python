
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

sembol=input("hangi coin isteniyorsa sembölünü giriniz")

sembol=sembol.upper()


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol':sembol
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '69d32df7-c4ad-4539-b9e1-6d24801e3714',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    parseData = json.dumps(response.json() )
    ethObj = json.loads(parseData)
    
    print(ethObj["data"][sembol]["name"])
    
    print(str(round(ethObj["data"][sembol]["quote"]["USD"]["price"],2) ) + " $")
    
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


time.sleep(5)
    
    
    
    