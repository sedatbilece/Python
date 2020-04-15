


class veribilimci():# clas oluşturma
    bolum=''
    sql='evet'
    deneyim=0
    diller=[]
    
veribilimci.sql # classa erişim

veribilimci.sql="hayir" # classı degiştirme

sedat=veribilimci2() # sınıf örneklerndirme


sedat.sql='degistir'
sedat.sql
sedat.diller.append("java") # !!! bu şekilde liste herkeste değişir
veli=veribilimci2()
veli.diller
 sedat.diller

class veribilimci2():
     def __init__(self): # herkese özel özellik için fonksiyon
         self.diller=[]
         
         
     def dilekle(self,yenidil):
        self.diller.append(yenidil)
sedat.diller.append("css")
veli.dilekle("r")


len()

class worker():
    def __init__(self,name,address): 
         self.name=name
         self.address=address
         
         

class datas(worker): # datas ın içine workerı yazarak worker içindekileri kullanabiliriz

    def __init__(self): 
         self.programming=''
         
veribilimci1=datas()
veribilimci1.name='sedat'
ali=worker("ali","hadımkoy")


new_sum= lambda a,b: a+b # fonksiyon tanımlama

new_sum(4,5)

a=[2,5,6,9]
b=[5,7,3,6]
ab=[]
for i in range(0,4):  
    ab.insert(i,a[i]*b[i]) # iki listenin aynı indexini çarpma işlemi
    
import numpy as np  # vektörel veri çarpma işlemi

a=np.array([2,5,6,9] )
b= np.array([5,7,3,6])
a*b

                        #----------->   map fonksiyonu
liste=[1,5,10,45]
list(map(lambda x: x+10,liste)    )# map komutu nesne üzerinde fonks çalıştırır



                         #-------------> filter


liste=[1,2,3,4,5,6,7,8,9,10]

list(    filter ( lambda x: x%2==0  , liste )      )    #filtreleme yapıldı



                        #------------>  reduce


from functools import reduce
         
 reduce(lambda a,b: a+b,liste)
    
 
 
  # modul çağırma
 
 #  1
 import hesapmodülü
 hesapmodülü.yenimaas()
 
 # 2
 
 from hesapmodülü import yenimaas
 yenimaas()
 
                   # hata kontrolü
 
 a=10
 b=0
 a/b
 
 y:
     a/b
     
except ZeroDivisionError:
    print("paydada sıfır var")
 
 
 
 
 
