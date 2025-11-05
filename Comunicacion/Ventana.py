from PyQt6.QtWidgets import QApplication, QMainWindow,QVBoxLayout,QWidget,\
    QHBoxLayout,QLabel, QTabWidget
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

        layout_horizontal_0 = QHBoxLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout_horizontal_0)

        caja1 = Caja("red")
        caja2 = Caja("yellow")

        tab_comunicacion = QTabWidget()
        tab_comunicacion.addTab(caja2, "Serie")

        tab_controladores = QTabWidget()
        tab_controladores.addTab(caja1, "Semaforo")

        layout_horizontal_0.addWidget(tab_comunicacion)
        layout_horizontal_0.addWidget(tab_controladores)
        

        #Enlazando con el worker
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
