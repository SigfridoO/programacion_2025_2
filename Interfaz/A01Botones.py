from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Presionname")
        
        # boton.clicked.connect(self.boton_clickeado)
        # boton.pressed.connect(self.boton_presionado)
        # boton.released.connect(self.boton_liberado)
        boton.clicked.connect(self.boton_alternado)
        boton.setCheckable(True)
        
        self.setCentralWidget(boton)
        
        self.resize(250, 200)
        #self.setMaximumSize(400,300) #Establecer tamaño de ventana
        #self.setWindowTitle("Mi programa de botones")  #Colocar titulo en la ventana
        #self.setFixedSize(400, 300) #Establecer tamaño fijo de ventana
        self.setWindowTitle("Mi programa de botones")
         
    def boton_alternado(self, valor):  
        print ("Valor", valor)
        
    def boton_clickeado(self):  
        print ("Boton clickeado")
        
    def boton_presionado(self):  
        print ("Boton presionado")
        
    def boton_liberado(self):  
        print ("Boton liberado")        
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()