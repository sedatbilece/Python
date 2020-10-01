import random
# işlemi bölerek bulma algoritması


liste=[]#liste oluşturduk


#0 ile 100 arasında elemanları olan dizi oluşturduk
for i in range(0,101):
    z=random.randint(0,1000)
    liste.append(z)
   
    

    

liste.sort()#liste sıralı olmalı 

ss=int(input("gir: ")) #aradığımız sayı

leng=len(liste)# uzunluk bulundu

mak=leng-1# max deger

minn=0# min deger

orta=int(mak/2)# ilk orta deger

while(1):
    
    print(orta)
    a=orta
    if(ss>liste[orta]):# büyükmü diye bakar büyükse:
        minn=orta# min deger orta indis olur
        mak# max aynen kalır
        
    elif(ss<liste[orta]):# kücükmü diye bakar büyükse:
        minn#min aynen kalır
        mak=orta# max orta deger olur
        
    elif(ss==liste[orta]):# eninde sonunda int degerlere ulasılır
        print("aranan sayı dizide var")#orta deger ss eşitse arama biter
        break
    orta=int((minn+mak)/2)
    if(a==orta):# orta hep aynı olursa sonsuz döngüden kurtulmak için
        break
    
    

    
