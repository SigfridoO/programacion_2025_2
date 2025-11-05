from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget
from PyQt6.QtCore import Qt

import sys

from pathlib import Path
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))
from Utils.Graficos import Caja


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QStackedLayout()
        contenedor = QWidget()
        contenedor.setLayout(self.layout)
        self.setCentralWidget(contenedor)

        caja1 = Caja("red")
        caja2 = Caja("orange")
        caja3 = Caja("cyan")
        caja4 = Caja("magenta")

        self.layout.addWidget(caja1)
        self.layout.addWidget(caja2)
        self.layout.addWidget(caja3)
        self.layout.addWidget(caja4)

        self.layout.setCurrentIndex(2)
        self.resize(250, 200)
        
    def keyPressEvent(self, event):
        indice = self.layout.currentIndex()
        indice_maximo = self.layout.count() - 1

        print("indice: ", indice)
        print("indice_maximo: ", indice_maximo)

        if event.key() == Qt.Key.Key_Left:
            indice = indice - 1

        if event.key() == Qt.Key.Key_Right:
            indice = indice + 1

        if indice > indice_maximo:
            indice = 0
        if indice < 0:
            indice = indice_maximo

        self.layout.setCurrentIndex(indice)
        event.accept()



def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
    
    

