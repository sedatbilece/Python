#octal_to_decimal

sayi2=input("sekizlik sayi gir")

uz=len(sayi2)

def sekizlik(sayi2):
    onluk=0
    a=0
    
    for i in range(uz-1,-1,-1):
        onluk+= (8**a)*int(sayi2[i])
        
        a+=1
    return onluk

print(sekizlik(sayi2))