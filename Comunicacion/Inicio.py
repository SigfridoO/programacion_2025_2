from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

from Ventana import Ventana
from Control import Control

class Inicio(Ventana):
    def __init__(self):
        super().__init__()
        print("Dentro de inicio")
        
        control = Control()
        control.iniciar()
        control.inicia_puerto_serie()
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()