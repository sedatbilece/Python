#binary_to_decimal

sayi=input("ikilik sayi gir")

uz=len(sayi)

def ikilik(sayi):
    onluk=0
    a=0
    
    
    for i in range(uz-1,-1,-1):
    
        if(sayi[i]=='1'):
            onluk+=2**a
        a+=1
    return onluk

print(ikilik(sayi))