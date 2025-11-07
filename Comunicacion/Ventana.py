from PyQt6.QtWidgets import QApplication, QMainWindow,QVBoxLayout,QWidget,\
    QHBoxLayout,QLabel, QTabWidget, QGridLayout, QPushButton
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

class VentanaSemaforo(QWidget):
    def __init__(self):
        super().__init__()

        layout_cuadricula = QGridLayout()
        self.setLayout(layout_cuadricula)

        caja2 = Caja("yellow")
        caja3 = Caja("blue")
        caja4 = Caja("magenta")
        caja5 = Caja("purple")
        caja6 = Caja("orange")
        caja7 = Caja("pink")
        caja8 = Caja("violet")

        self.boton_encender = QPushButton("Encender")
        self.boton_apagar = QPushButton("Apagar")

        layout_vertical_1 = QVBoxLayout()
        layout_vertical_1.addWidget(caja3)
        layout_vertical_1.addWidget(caja4)
        layout_vertical_1.addWidget(caja8)


        layout_cuadricula.addWidget(caja2, 0, 0, 3, 1)
        layout_cuadricula.addWidget(self.boton_encender, 0, 1)
        layout_cuadricula.addWidget(self.boton_apagar, 1, 1)
        layout_cuadricula.addWidget(caja5, 2, 1)
        layout_cuadricula.addLayout(layout_vertical_1, 0, 2, 3, 1)
        layout_cuadricula.addWidget(caja7, 3, 0, 1, 3)

        self.worker = None

    def establecer_worker(self, worker):
        self.worker = worker
        if self.worker:
            self.worker.senales.luz_indicador.connect(self.cambiar_indicador)


    def cambiar_indicador(self, estado : bool):
        if estado:
            self.modificador_indicador(self.caja_0, "green")
            pass
        else:
            self.modificador_indicador(self.caja_0,"gray")
            pass

    def modificador_indicador(self, indicador:QLabel,color:str ):
        indicador.setStyleSheet(f"background-color: {color} ; border-radius: 20")


class Ventana(QMainWindow):
    def __init__ (self):
        super().__init__()

        layout_horizontal_0 = QHBoxLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout_horizontal_0)

        caja1 = Caja("red")


        self.ventana_semaforo = VentanaSemaforo()

        tab_comunicacion = QTabWidget()
        tab_comunicacion.addTab(caja1, "Serie")

        tab_controladores = QTabWidget()
        tab_controladores.addTab(self.ventana_semaforo, "Semaforo")

        layout_horizontal_0.addWidget(tab_comunicacion)
        layout_horizontal_0.addWidget(tab_controladores)

        #self.cambiar_indicador(True)
        
        self.setCentralWidget(contenedor)
        self.resize(400, 250)

        #Enlazando con el worker
        self.threadpool = QThreadPool()
        self.worker = Worker()
        self.threadpool.start(self.worker)

    def obtener_worker(self):
        return self.worker




def main():
    print("Dentro de main")
    app = QApplication (sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__== "__main__":
    main()
