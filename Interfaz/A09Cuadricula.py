from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
import sys

from pathlib import Path
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))
from Utils.Graficos import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        layout_rejilla = QGridLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout_rejilla)

        caja1 = Caja("red")
        caja2 = Caja("blue")
        caja3 = Caja("orange")
        caja4 = Caja("green")
        caja5 = Caja("cyan")

        layout_rejilla.addWidget(caja1, 0,0, 2, 2)
        layout_rejilla.addWidget(caja2, 2,1, 1, 2)
        layout_rejilla.addWidget(caja3, 0, 3)
        layout_rejilla.addWidget(caja4, 1, 3)
        layout_rejilla.addWidget(caja5, 2, 3)

        self.setCentralWidget(contenedor)
        self.resize(250, 200)
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
    
    
