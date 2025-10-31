from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont

import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        etiqueta = QLabel("Certificación")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter \
            | Qt.AlignmentFlag.AlignHCenter)
        fuente = QFont("Times New Roman", 20, QFont.Weight.Bold, italic=True) #:D
        etiqueta.setFont(fuente) #Definir tipo de letra y tamaño de letra
        self.setCentralWidget(etiqueta)
        
        ruta = abs_path("cat.jpg")
        print("ruta: ", ruta)
        imagen = QPixmap(ruta)
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)
        self.setCentralWidget(etiqueta)
        self.resize(250, 200)
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
