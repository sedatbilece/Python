
   # asal sayi bulucu
sayi=int(input("bir sayi giriniz"))
x=0
for i in range(2,sayi):
    if(sayi%i==0):
        x+=1
if(x==0):
    if(sayi!=1):
        print(sayi,"  sayisi asal sayıdır")
        
    
    
else:
    print(sayi,"  sayisi asal sayı değildir")
        
    

        
    
# sayinin tam bölenleri
    
sayi=int(input("bir sayi giriniz"))
    
    
for i in range(1,sayi+1):
        if(sayi%i==0):
            print("sayının bölenleri = ",i)