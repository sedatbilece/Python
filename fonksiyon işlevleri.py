list=["a",9,4,6,8]

dir(list)#içindeki eleman ile neler yapılabilecegi (  list.fonksiyon  ) 
list=list+[11]
list
del list#listeyi sil
del list[0]# index li elemanı sil
list.append(12)# direk ekleme

list.remove("a")# elemana göre çıkarma

list.insert(0,"bbbb") #indexe göre ekle

list.pop(2)  #indexe göre çıkar

   uzunluk =len(list) #uzunluk bul
   
list.insert(uzunluk,"sedat") 

listeyedek=list.copy()#liste kopyala

list.index("sedat") # eleman indexini ver

list.reverse()#elemanları terse çevir

list.pop(0)

list.sort()# elemanları sıralar

list.clear()# liste için boşalt



ad="sedat"
ad.upper()#string içindeki harfleri büyültür

ad.lower()#string içindeki harfleri küçültür

ad.islower()#küçük mü diye bakar hepsi küçükse true 1 verir

ad.isupper()#buyuk mü diye bakar hepsi büyükse true 1 verir
    
ad.replace("e","a") #harflere yeni deger atar

ad.strip("s") #kesme yapar hiçbişi tanımlanmazsa bas ve sondaki boşlukları keser





#   ^^^^  tuple  ^^^^  (listeler ile aynı tek farkı değiştirelemez)

t= ("a",3,1.4,[1,2,3])

tupnot=("sedat")# bu str olur

tupis=("sedat",) # bu tuple olur (sona virgül gerek)

t[1]
t[1:3]# erişmeler liste ile aynı

t[2]=99 # hata verir atama yapılmaz





#             Dictionary (Sözlük)


 #                  ----------------------> dic = {keyword : item }


sozluk={"s":"sedat"  ,  "v":[10,20,"vedat"]  ,  "f": 20  ,  21 :"asd"} #sözlük oluşturma
len(sozluk)

sozluk[21]="dsssss"
q= sozluk[21]

sozluk


sozlukic={"a":{"h":10,"j":20,"k":30}, #iç içe sözlükler 
          
          "b":{"h":10,"j":20,"k":30},
          
          "c":{"h":10,"j":20,"k":30}}


sozlukic["a"]["k"]

sozluk["ist"]="istanbul" # eleman ekleme

sozluk["s"]="SEDAT B"  # eleman değiştirme veya atama




#   -------------->  set =set(liste,tuple,dic herhangi biri)




s=set()   # set oluşturuldu


 str="sedat başkan"
l=[1,3,5,7,9,1]  

s=set(l)# atama yapıldı
s=set(str)
len(s)
s
ısı =["sedat","bilece"]
s=set(ısı[0])

set1=set([1,4,9,7,3])
set2=set([3,8,4,5])

set1.difference(set2) #set1 in set2 den farkını verir 

set1.symmetric_difference(set2) # ikisindede olan farklı elemanları veiri 
set2-set1 # bu şekildede fark alınabilir 

set1.intersection(set2)  # kesişimleri verir 
 xxx =set1 & set2 # bu şekildede kesişim alınabilir 

set1.union(set2) # birleşim 

set1=set1.intersection(set2)

set1.isdisjoint(set2) #kesişimleri oldugu için false döner

set1.issubset(set2) #set1 set2 nin alt kümesimi diye bakar (





#          ------> kapsayıcı    sıralı    değiştirilebilir <---------         #

#     list=[]          yes        yes           yes

#     tuple=()         yes        yes           no

#     dictionary={}    yes        no            yes

#     set=set()        yes        no            yes      eşşiz eleman içerir










