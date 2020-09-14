from PyQt5 import  QtWidgets
from PIL import Image,ImageFilter
import sys
import os
#################################pencere class ı

class pencere(QtWidgets.QWidget):
    
    def __init__(self):
        
        
        super().__init__()#QtWidgets.QWidget init fonk cağrıldı
        
        self.init_ui()#def init_ui(self): çağrıldı
        
        
    def init_ui(self):
        
        ###################### obje olusturma
        
        self.dosya_sec=QtWidgets.QPushButton("Dosya Seç")
        
        
        
        self.x1=QtWidgets.QLineEdit()
        
        self.boyut=QtWidgets.QPushButton("b1xb2 |boyutu ayarla")
        
        
        self.blursev=QtWidgets.QLineEdit()
        self.blurbut=QtWidgets.QPushButton("1-5| blurla")
        
        self.siyahla=QtWidgets.QPushButton("siyah beyaz yap")
        
        self.image=""
        self.dosya_ismi=[]
        
        ################################ objelerin eklenmesi
        vbox=QtWidgets.QVBoxLayout()
        
        vbox.addWidget(self.dosya_sec)
        
        
        
        
        
        vbox.addStretch()
        
        hbox2=QtWidgets.QHBoxLayout()
        hbox2.addWidget(self.x1)
        hbox2.addWidget(self.boyut)
        vbox.addLayout(hbox2)
        vbox.addStretch()
        
        hbox3=QtWidgets.QHBoxLayout()
        hbox3.addWidget(self.blursev)
        hbox3.addWidget(self.blurbut)
        vbox.addLayout(hbox3)
        vbox.addStretch()
        
        vbox.addWidget(self.siyahla)
        
        self.dosya_sec.clicked.connect(self.secfok)
        
        self.boyut.clicked.connect(self.secfok)
        self.blurbut.clicked.connect(self.secfok)
        self.siyahla.clicked.connect(self.secfok)
        
        self.setLayout(vbox)
        
    
        ########################### pencere işlemleri
    
        self.setWindowTitle("Resim İşleme") # pencere adı
        
        self.setGeometry(200,200,300,300) # boyut ve konumu
        self.show()
        
    def secfok(self):# butonlara basılınca yapılacak işlemler
        a=self.sender().text()
        
        if(a=="Dosya Seç"):
            
            self.dosya_ismi=QtWidgets.QFileDialog.getOpenFileName(self,"dosya aç",os.getenv("desktop"))
            self.image=Image.open(self.dosya_ismi[0])
            print(self.dosya_ismi[0])
            
            
            
        
            
        elif a=="siyah beyaz yap": #working
            self.image.convert(mode="L").save(self.dosya_ismi[0])
            print("siyah beyaz yap")
            
        elif a=="1-5| blurla":# working
            self.image.filter(ImageFilter.GaussianBlur(int(self.blursev.text()))).save(self.dosya_ismi[0])
            print("1-5| blurla")
            
        elif a=="b1xb2 |boyutu ayarla":#working
            print("b1xb2 |boyutu ayarla")
            x2=str(self.x1.text())
            
            x2=x2.split("x")
            a=int( x2[0])
            b=int(x2[1])
        
            self.image.thumbnail((a,b))# boyut değiştirme
            self.image.save(self.dosya_ismi[0])
            
            
            
            
            
        
app=QtWidgets.QApplication(sys.argv)

pencere=pencere()

sys.exit(app.exec_())

      
        