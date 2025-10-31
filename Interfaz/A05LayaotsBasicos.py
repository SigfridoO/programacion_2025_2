from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget
import sys

from pathlib import Path
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))
from Utils.Graficos import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout)
        
        caja_1 = Caja("black")
        caja_2 = Caja("#7C12D3")
        caja_3 = Caja("#12D383")
        
        layout.addWidget(caja_1)
        layout.addWidget(caja_2)
        layout.addWidget(caja_3)
        
        layout.setContentsMargins(10, 10, 10, 0)   #Establecer margenes a los lados
        layout.setSpacing(10) #Espaciamiento entre caja y caja+
         
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
 