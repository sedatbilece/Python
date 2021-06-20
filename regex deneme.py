import re

dir(re)

metin="aşk olmadan meşk olmaz"
 
# ------------------------------------------

kontrol=re.match("aşk",metin)

print(kontrol)# ifade

 
print(kontrol.span())#kelimenin hangi aralıkta olduğu


print(kontrol.group())# aranan kelimeyi döndürür

print("********")
# ------------------------------------------

kontrol=re.match("meşk",metin)# match eşleştirme yapar

print(kontrol)#  None döndürür

print("********")
# ------------------------------------------

kontrol=re.search("meşk",metin)#search arama yapar


print(kontrol.span())# 

print("********")
# ------------------------------------------

liste=["kedi","köpek","fare"]

for i in liste:
    kntrol=re.search("kedi", i)
    print(kntrol)

print("********")
# ------------------------------------------

met="ilim bilim bilmektir"

knt=re.findall("ilim",met)# metindeki kelimelerin listesini döndürür

print(knt)

print("********")
# ------------------------------------------
liste=["sezin","selin","salih","metin"]

for i in liste:
    if re.search("se[zl]in",i):# [] yapıp içine verilenlerden 
        print(i)#herhangi biri olur anlamında
        
print("********")
# ------------------------------------------
liste=["sezin","selin","salih","metin"]

for i in liste:
    if re.search("me.in",i):# . herhangi bir harfin yerini tutar
        print(i)
        
print("********")

# ------------------------------------------
liste=["sezin","selin","salih","metin"]

for i in liste:
    if re.search("se?",i):# 
        print(i)
         
print("********")

re.search("se*",i):#  s olacak e 0 yada daha fazla karakteri bulur
re.search("se+",i):# s olacak e 1 yada daha fazla karakteri bulur 
re.search("se?",i):#  s olacak e 0 yada daha fazla karakteri bulur


# ------------------------------------------
print("********")

liste=["seezin","selin","salih","metin"]

for i in liste:
    if re.search("se{2}",i):# kendinden önceki kelime adedi
        print(i)



 if re.search("^se",i):#se ile başlayan karakteri döndürür
 if re.search("n$",i):# n ile biten strigi döndürür
# ------------------------------------------
print("********")

metin ="arabayı 15000$ a aldım"
print(re.findall("[0-9]+\$", metin))#0 ile 9 arasındaki 
# karakter ile  başlayan ve $ işareti ile biten metin


# ------------------------------------------
print("********")
 

liste=["seezin","selin","salih","metin"]

for i in liste:
    if re.search("^se|in$",i):# | veya anlamında
        print(i)







