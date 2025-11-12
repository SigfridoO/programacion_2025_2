
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QWidget, QLabel, QPushButton
import sys

class VentanaRasp (QWidget):
    def __init__(self):
        super().__init__()
        layout_horizontal_1 = QHBoxLayout()
        layout_vertica_1 = QVBoxLayout()

        boton_activar = QPushButton("Activar")
        boton_desactivar = QPushButton("Desactivar")

        etiqueta_salida = QLabel()
        etiqueta_salida.setStyleSheet(f"background-color: {"#9EBE97"}")

        self.setLayout(layout_horizontal_1)
        layout_horizontal_1.addLayout(layout_vertica_1)
        layout_horizontal_1.addWidget(etiqueta_salida)
        layout_vertica_1.addWidget(boton_activar)
        layout_vertica_1.addWidget(boton_desactivar)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        ventana_rasp = VentanaRasp()
        self.setCentralWidget(ventana_rasp)
        self.resize(250, 200)
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
    
    
