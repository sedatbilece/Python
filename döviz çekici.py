import time
import requests
import json

url="https://api.exchangeratesapi.io/latest?base=USD"

res=requests.get(url)


res=json.loads(res.text)


print("1 dolar : "+str(res["rates"]["TRY"])+" tl")

usd=res["rates"]["TRY"]
url="https://api.exchangeratesapi.io/latest?base=EUR"

res=requests.get(url)


res=json.loads(res.text)
print("1 euro : "+str(res["rates"]["TRY"] )+" tl")

url="https://metals-api.com/api/latest?access_key="yours key is here"# bunu kendi keyiniz ile değiştirmeniz gerekli


res=requests.get(url)


res=json.loads(res.text)
print("ons altın : {} dolar".format(res["rates"]["USD"]))

gold=res["rates"]["USD"]

gram =gold/31.1

print("1 gr altın:"+str(gram*usd)+" tl")

time.sleep(3)
