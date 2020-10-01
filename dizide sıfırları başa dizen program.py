liste=[1,0,6,-4,8,0,7,0,9,0,6,8]

leng= len(liste)//uzunlugu bulduk
count=0//sıfırları yazarken dizide nerde olacağımızı belirleyecek


for i in range(0,leng):
    
    if(liste[i]==0)://i.ninci eleman sıfır ise
        
        temp=liste[count] //listenin countıncı elemanını sakla
        
        liste[count]= liste[i]//listenin countıncı elemanına 0 ata
        
        liste[i]=temp // sıfırı aldığımız indexe saklananı ata
        
        count+=1  //bulunduğumuz indexi bir arttır

//yazdırma işlemi
for i in liste:
    print(i)
        
