s1 = int(input("sayi1:  "))
s2 = int(input("sayi2: "))
snc = 0

while s2 != 0:# ikinci sayı 0 değilse

   if (s2%2 != 0):#2. yani bölünen sayının modu 0 deği ise yani tek ise
      snc=snc+s1
      s1=s1*2 #ilk sayı çarpılır
      s2=int(s2//2)# ikinci sayı 2ye bölünür // float değer olmaması için
      
   if (s2%2 == 0):# moddan kalan 0 ise yani 2. değer çiftse bölünenen
      s1=s1*2
      s2=int(s2//2)

print("sonuc: ",(snc))
