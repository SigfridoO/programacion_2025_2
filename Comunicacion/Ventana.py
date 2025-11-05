from PyQt6.QtWidgets import QApplication, QMainWindow,QVBoxLayout,QWidget,QHBoxLayout,QLabel
import sys
from PyQt6.QtCore import QRunnable, QThreadPool,pyqtSignal as Signal, QObject,Qt
from pathlib import Path
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))

from Utils.Graficos import Caja


class WorkerSignals(QObject):

    luz_indicador = Signal(bool)

    def __init__(self):
        super().__init__()

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.senales = WorkerSignals()

    def run(self):
        pass

    def prender_indiccador(self,estado:bool = False):
        try:
            self.senales.luz_indicador.emit(estado)
        except Exception as e:
            print("Se obtuvo un error")

class Ventana(QMainWindow):
    def __init__ (self):
        super().__init__()

        layout_vertical_0 = QVBoxLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout_vertical_0)
        


        self.caja_0 = Caja("gray")
        self.caja_0.setFixedSize (40, 40)
        caja_1 = Caja("orange")
        caja_2 = Caja("pink")

        layout_horizontal_0 = QHBoxLayout()
        layout_horizontal_0.addWidget(self.caja_0)
        layout_horizontal_0.addWidget(caja_1)

        layout_vertical_0.addLayout(layout_horizontal_0)
        layout_vertical_0.addWidget(caja_2)

        #Enlasando con el worker
        self.threadpool = QThreadPool()
        self.worker = Worker()
        self.worker.senales.luz_indicador.connect(self.cambiar_indicador)
        self.threadpool.start(self.worker)

        #self.cambiar_indicador(True)
        
        self.setCentralWidget(contenedor)
        self.resize(250, 200)

    def obtener_worker(self):
        return self.worker

    def cambiar_indicador(self, estado : bool):
        if estado:
            self.modificador_indicador(self.caja_0, "green")
            pass
        else:
            self.modificador_indicador(self.caja_0,"gray")
            pass

    def modificador_indicador(self, indicador:QLabel,color:str ):
        indicador.setStyleSheet(f"background-color: {color} ; border-radius: 20")


def main():
    print("Dentro de main")
    app = QApplication (sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__== "__main__":
    main()
