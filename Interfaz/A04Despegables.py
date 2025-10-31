from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        despegable = QComboBox()
        despegable.addItems(['Opcion 1', 'Opcion 2', 'Opcion 3'])
        despegable.currentIndexChanged.connect(self.indice_seleccionado)
        despegable.currentTextChanged.connect(self.texto_seleccionado)
        self.setCentralWidget(despegable)
        self.resize(250, 80)
    
    def indice_seleccionado(self, indice):
        print("Indice seleccionado: ", indice)   #En terminal indica el indice seleccionado
          
    def texto_seleccionado(self, texto) :
        print("Texto seleccionado: ", texto)   #En terminal indica el texto seleccionado
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
 