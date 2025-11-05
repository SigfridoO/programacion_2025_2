from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
import sys

from pathlib import Path
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))
from Utils.Graficos import Caja


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        contenedor = QTabWidget()

        caja1 = Caja("green")
        caja2 = Caja("red")
        caja3 = Caja("orange")

        contenedor.addTab(caja1, "verde")
        contenedor.addTab(caja2, "rojo")
        contenedor.addTab(caja3, "naranja")

        contenedor.setMovable(True)
        contenedor.setTabPosition(QTabWidget.TabPosition.South)

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
    
    