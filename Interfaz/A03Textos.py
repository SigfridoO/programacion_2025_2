from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.texto = QLineEdit()
        self.texto.textChanged.connect(self.texto_cambiado)
        self.texto.returnPressed.connect(self.texto_presionado)
        
        self.setCentralWidget(self.texto)
        self.resize(400, 80)
        
    def texto_cambiado(self,text):  
        print(text)  
        
    def texto_presionado(self):  
        self.setWindowTitle(self.texto.text())     
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
    