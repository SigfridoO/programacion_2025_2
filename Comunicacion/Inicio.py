from PyQt6.QtWidgets import QApplication, QMainWindow,QBoxLayout, QWidget,QVBoxLayout
import sys
from Ventana import Ventana
from Control import Control



class Inicio (Ventana):
    def __init__(self):
        super().__init__()
        print("Dentro de Inicio")

        control = Control()
        control.iniciar()
        control.iniciar_puerto_serie()
        control.establecer_worker(self.obtener_worker())
         

def main():
    print("Dentro de main")
    app = QApplication (sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()