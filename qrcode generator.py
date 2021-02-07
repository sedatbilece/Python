from PyQt5 import  QtWidgets

import sys
import qrcode



class pencere(QtWidgets.QWidget):
    
    def ifkaydet(self):
            mytext = self.yazi.toPlainText()
            img=qrcode.make(mytext)
            img.save("myqrcode.png")
            
    
    
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        
        
    def init_ui(self):
        self.yazi=QtWidgets.QTextEdit()
        self.kaydet=QtWidgets.QPushButton("kaydet")
        
        vbox=QtWidgets.QVBoxLayout()
        vbox.addWidget(self.yazi)
        vbox.addWidget(self.kaydet)
        
        self.setLayout(vbox)
        self.setWindowTitle("qr kod olusturucu ")
        
        self.kaydet.clicked.connect(self.ifkaydet)
        
        
        self.show()
        
app=QtWidgets.QApplication(sys.argv)

pencere=pencere()

sys.exit(app.exec_())
