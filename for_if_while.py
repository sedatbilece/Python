4*4 
4**4 # 4 Ã¼zeri 4 demek 256 verir

def kareal(x):
    print(x**2)
    
 kareal(6)
 
 # açıklama ile sayı bastırma 
 

def kareal(x):
    print("girilen sayının karesi:"+ str(x**2))
    
 kareal(6)
 def kareal(x):
    print("girilen sayı: " +  str(x)  +  " karesi: " +  str(x**2)   )
    
 kareal(6)
 
 def carpma(x,y=1): # y için deger verilmezse y'yi 1 alır
    
     print(x*y)
     
carpma(6,7)

carpma(y=5,x=7) #bu şeilde sıradan baağımsızda veilebilir


def kareal(x):    # return kullanımı
    print(x**2)
    return (x**2)
    
 a= kareal(6)
print(a)


x=[]
def ekle(y):
    x.append(y)
    
ekle(9)

sinir=5 # sinira 5 degeri atandı

 sinir==4  # sinir 4 mü diye soruldu
 
  #               if
 
     a=3
     b=2
if a>b:
    print("a b den buyuktur")
    
 #                 else
    
     a=2
     b=2
if a==b:
    print("a b ye esit")

elif a>b:
    print("a b den buyuk")    

else:
    print("a b ye esit DEGIL")
    
    
    #                     for DÖNGÜSÜ
    
    ogrenci=["ali","veli","mahmut","kamil"]

      for i in ogrenci:
          print(i)
          
string  ="gollum"

for i in string:
    print(i)
   
    
for i in range(10):  # 0 dan 9 a kadar basar
    print(i)
    
for i in range(4,20):  # 4 ten 19 a kadar basar
    print(i)
    
for i in range(10,100,5):  # 10 dan 95 e kadar 5 er 5er atlayarak gider
    print(i)
    
# maas artttırma uygulaması      
    

maaslar=[1000,5000,4000,7000,9000]

def zam(y):  # zam yeni maas fonksiyonu
    x=y+((y*20)/100)    
    return x
z=0
for i in maaslar:
  print(i)
  print(zam(i))
  f= zam(i)# fonks dönen yeni maas
  maaslar.pop(z) # zninci eleman silindi
  maaslar.insert(z,f) # zninci elemana yeni maas f eklendi
  z=z+1
  if z==5:
      z=0
      break
  
    
    
    #                  while
  say=1
 while say <10:
        say+=1
        print(say)
        
        


 #            break ve continue

 if z==5:
      z=0
      break
  

  
    
    
    
  