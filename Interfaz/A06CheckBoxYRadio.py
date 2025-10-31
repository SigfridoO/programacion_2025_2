from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QPushButton, QRadioButton, QCheckBox, \
        QGroupBox, QHBoxLayout, QVBoxLayout, QWidget
import sys

from pathlib import Path 
ruta = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta))

from Utils.Graficos import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        contenedor_principal = QWidget()
        layout_vertical_0 = QVBoxLayout()
        contenedor_principal.setLayout(layout_vertical_0)
        
        caja1 = Caja("#5386B5D5")
        caja2 = Caja("#8157E2FF")
        
        layout_horizontal_1 = QHBoxLayout()
        
        grupo_radio = QGroupBox("Materia preferida")
        layout_vertical_1 =QVBoxLayout()
        grupo_radio.setLayout(layout_vertical_1)
        radio_maquinas = QRadioButton("1. Máquinas eléctricas")
        radio_seguridad = QRadioButton("2. Seguridad e Higiene")
        radio_manufactura_avanzada = QRadioButton("3. Manufactura avanzada")
        radio_manufactura_asistida = QRadioButton("4. Manufactura asistida")
        radio_taller = QRadioButton("5. Taller de investigación")
        radio_programacion = QRadioButton("6. Programación avanzada")

        
        layout_vertical_1.addWidget(radio_maquinas) #AGREGAR OPCION A PANTALLA
        layout_vertical_1.addWidget(radio_seguridad)  #AGREGAR OPCION A PANTALLA
        layout_vertical_1.addWidget(radio_manufactura_avanzada) #AGREGAR OPCION A PANTALLA
        layout_vertical_1.addWidget(radio_manufactura_asistida) #AGREGAR OPCION A PANTALLA
        layout_vertical_1.addWidget(radio_taller) #AGREGAR OPCION A PANTALLA
        layout_vertical_1.addWidget(radio_programacion) #AGREGAR OPCION A PANTALLA
        
        ###################################################################################
        grupo_checkbox = QGroupBox("HOBBYS")
        layout_vertical_2 =QVBoxLayout()
        grupo_checkbox.setLayout(layout_vertical_2)
        
        check_videojuegos = QCheckBox("1. Videojuegos")
        check_musica = QCheckBox("2. Escuchar música")
        check_bailar = QCheckBox("3. Bailar")
        check_programar = QCheckBox("4. Programar")
        check_dormir = QCheckBox("5. Dormir")
        check_leer = QCheckBox("6. Leer")

        
        layout_vertical_2.addWidget(check_videojuegos) #AGREGAR OPCION A PANTALLA
        layout_vertical_2.addWidget(check_musica)  #AGREGAR OPCION A PANTALLA
        layout_vertical_2.addWidget(check_bailar) #AGREGAR OPCION A PANTALLA
        layout_vertical_2.addWidget(check_programar) #AGREGAR OPCION A PANTALLA
        layout_vertical_2.addWidget(check_dormir) #AGREGAR OPCION A PANTALLA
        layout_vertical_2.addWidget(check_leer) #AGREGAR OPCION A PANTALLA
        
        layout_horizontal_1.addWidget(grupo_radio) #Se imprimen en el layout
        layout_horizontal_1.addWidget(grupo_checkbox) 
        
        layout_horizontal_2 = QHBoxLayout()
        layout_horizontal_2.addWidget(QPushButton("Aceptar"))
        layout_horizontal_2.addWidget(QPushButton("Cancelar"))
        layout_horizontal_2.addWidget(QPushButton("Aplicar"))
        
        layout_vertical_0.addLayout(layout_horizontal_1)
        layout_vertical_0.addLayout(layout_horizontal_2)
        
        
        self.setCentralWidget (contenedor_principal)
        self.resize(350, 300)
        
def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
 
if __name__ == "__main__":
    main()
 