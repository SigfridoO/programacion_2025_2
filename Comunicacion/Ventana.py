from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, \
    QHBoxLayout, QLabel
import sys

from pathlib import Path
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))

from Utils.Graficos import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.resize(250, 200)
        layout_vertical_0 = QVBoxLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout_vertical_0)
        
        self.caja_0 = Caja("gray")
        caja_1 = Caja("orange")
        caja_2 = Caja("pink")
        
        layout_horizontal_0 = QHBoxLayout()
        layout_horizontal_0.addWidget(self.caja_0)
        layout_horizontal_0.addWidget(caja_1)
        
        layout_vertical_0.addLayout(layout_horizontal_0)
        layout_vertical_0.addWidget(caja_2)
        
        self.cambiar_indicador(True)
        self.setCentralWidget(contenedor)
        self.resize(250, 200)
        
    def cambiar_indicador(self, estado: bool):
        if estado:
            self.modificar_indicador(self.caja_0, "green")
            pass
        else:
            self.modificar_indicador(self.caja_0, "gray")
            pass
        
    def modificar_indicador(self, indicador:QLabel, color:str):
        indicador.setStyleSheet(f"background-color: {color}")

def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()