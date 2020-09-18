import sqlite3 

con= sqlite3.connect("vertab.db")

cursor=con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (idsi INT,isim TEXT,yazar TEXT) ")
con.commit() 

xy=0

def yazdir():
    print("---> yapılacak işlemi tuşlayın :")
    print("1-) kitap ekle \n 2-)kitap sil\n 3-)kitapları listele \n 4-)çıkış")
    vals=int(input("1 2 3 4 birini tuşlayın = "))
    return vals

while 1:
    
    xy=yazdir()
    
    
    if xy==1:
        
        cursor.execute("SELECT *FROM kitaplık")
        liste=cursor.fetchall()
        
            
        
        if(len(liste) > 0 ):
            idsi= len(liste)+1
        else:
            idsi=1
        
        
        
        isim=input("isim ")
        yazar=input(" yazar")
        
        for i in liste:
            if(isim==i[1]):
                print("eşleşen isim bulunmakta")
                break
            
        
        
        
        cursor.execute("INSERT INTO kitaplık VALUES (?,?,?) " ,(idsi,isim,yazar) )
        con.commit()
        print("işlem tamamlandı")
        
    elif xy==2:
        isim=input("silinecek kitap ismini giriniz ...")
        cursor.execute("Delete From kitaplık Where isim= ?",(isim,))
        con.commit()
    
    elif xy==3:
        cursor.execute("SELECT *FROM kitaplık")
        print("\n********************************\n")
        liste=cursor.fetchall()
        for i in liste:
            print(i)
        print("\n********************************\n")
        
    elif xy==4:
        print(" program bitti")
        break
        
    else:
        print("lütfen istenen numaralardan birini tuşlayın")
        
con.close()
        




        
    
    
    
    
    
    
    
    

    
  

        