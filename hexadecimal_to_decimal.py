 #hexadecimal_to_decimal

sayi3=input("onaltılık sayi gir")

uz=len(sayi3)

def onaltilik(sayi3):
    onluk=0
    a=0
    
    for i in range(uz-1,-1,-1):
        x=sayi3[i]
        if(x=='A'):
            onluk+= (16**a)*10
        elif(x=='B'):
            onluk+= (16**a)*11
        elif(x=="C"):
            onluk+= (16**a)*12
        elif(x=="D"):
            onluk+= (16**a)*13
        elif(x=="E"):
            onluk+= (16**a)*14
        elif(x=="F"):
            onluk+= (16**a)*15
        else:
            onluk+= (16**a)*int(sayi3[i])
        a+=1
    return onluk
    
print(onaltilik(sayi3))