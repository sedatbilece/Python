import sys

sys.exit()# programı bitirir

sys.stdout.write("normal mesaj \n") # çıktı alırız bu özellikler c den gelir

sys.stderr.write("hata mesajı\n")

for i in sys.argv:#dosyayı cmd den çalıştırırken verdiğimiz argümanları listeler 
    print(i)#ilk eleman dosynın adı
    
    
print(sys.argv)

sys.executable# python ın çalıştığı dizini döndürür

sys.getwindowsversion()# windows sürümü özelliklerini döndürür

sys.platform# programın çalıştığı platformu döndürür

sys.prefix# pythonın nerede kurulu olduğunu döndürür

vers =sys.version# kullanılan python sürümünü döndürür
print(vers)


sys.path


for i in sys.modules: #sys.modules modülleri listeler
    print(i)
    
    

    

