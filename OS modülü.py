import os
from datetime import datetime

print( dir(os) )

os.name


print(os.getcwd() )#hangi diznde olduğumuzu döndürür !!!!! \ ile döndürür

os.chdir("C:/Users/sedat/Desktop") # dizi değiştirme  !!!! veri girişi / ile


print(os.listdir( )  ) # dizindeki elemanları listeler

os.mkdir("deneme1")# klasör oluşturma

os.makedirs("deneme2/deneme3")# deneme2 altında deneme3 klasörünü oluşturur

os.rmdir("deneme2/deneme3")# deneme2 altında deneme3 klasörünü siler 

os.removedirs("deneme2/deneme3")#ikisini birden siler

os.rename("test.txt","test2.txt")# isim değiştirme

os.stat("test2.txt")# dosya özelliklerini döndürür

########################################## dosyanın değitirilme zamanını alma
time= os.stat("test2.txt").st_mtime

timenormal=datetime.fromtimestamp(time)

print(timenormal)
######################################### dizindeki dosyaları liste döndürme

os.walk("C:/Users/sedat/Desktop")# generetor dönderir


for i,j,k in os.walk("C:/Users/sedat/Desktop"):
    print(i)#klasör yolu
    print(j)#klasör isimleri
    print(k)#dosya isimleri
    print("*********************")
    
    

    






