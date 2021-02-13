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

url="https://metals-api.com/api/latest?access_key=a3i39z54h6lia8crziu2itj1e9p20sdt2985fkg43n2yae0yej8o32zmql3t&base=XAU&symbols=USD"


res=requests.get(url)


res=json.loads(res.text)
print("ons altın : {} dolar".format(res["rates"]["USD"]))

gold=res["rates"]["USD"]

gram =gold/31.1

print("1 gr altın:"+str(gram*usd)+" tl")

time.sleep(3)
