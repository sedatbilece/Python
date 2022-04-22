# -*- coding:utf-8 -*-

import re
kelime=" kitap"
kelime2=" Kitap"
dosyayolu=input("dosya adini giriniz:")

with open(dosyayolu+".txt",encoding="utf8") as f:
    text = f.read()

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
cnt=0
fp=open(dosyayolu+"-split.txt", 'w')
for i in sentences:
    snc=i.find(kelime)
    snc2=i.find(kelime2)
    
    if(snc>0 or snc2>0):
        fp.write(i)
        fp.write("\n")
        fp.write("*")
        fp.write("\n")
        cnt+=1
        

    
    
    print("step: "+str(cnt))
   
    
    
f.close()
fp.close()