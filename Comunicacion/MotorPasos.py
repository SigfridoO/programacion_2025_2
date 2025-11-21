
from enum import Enum
import threading
import time

from Electronica import Electronica

class estadoMotor(Enum):
    home = 0
    estado_1 = 1
    estado_2 = 2
    estado_3 = 3
    estado_4 = 4
    estado_5 = 5
    estado_6 = 6
    estado_7 = 7
    estado_8 = 8

class MotorPasos:
    def __init__(self):
        self.bobina_A = False
        self.bobina_B = False
        self.bobina_C = False
        self.bobina_D = False

        self.z0_arranque = True
        self.z1_direccion = False
        self.z2_enclavamiento = False

        self.estado_actual = estadoMotor.home
        self.cuenta = 0
        self.funcionando = False
        self.contador = 0
        self.electronica = None

        self.tarea = threading.Thread(target = self.motor_funcionando)

    def activar_motor(self):
        self.tarea.start()

    def motor_funcionando(self):
        print("Dentro de la funcion motor funcionando")
        self.funcionando = True
        while self.funcionando and self.contador < 401:
            
            if self.z0_arranque:
                # Iniciar el movimiento
                estado_aux = self.estado_actual
                match estado_aux:
                    case estadoMotor.home:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_1
                        else:
                            self.estado_actual = estadoMotor.estado_1

                    case estadoMotor.estado_1:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_8
                        else:
                            self.estado_actual = estadoMotor.estado_2

                    case estadoMotor.estado_2:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_1
                        else:
                            self.estado_actual = estadoMotor.estado_3

                    case estadoMotor.estado_3:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_2
                        else:
                            self.estado_actual = estadoMotor.estado_4

                    case estadoMotor.estado_4:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_3
                        else:
                            self.estado_actual = estadoMotor.estado_5

                    case estadoMotor.estado_5:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_4
                        else:
                            self.estado_actual = estadoMotor.estado_6

                    case estadoMotor.estado_6:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_5
                        else:
                            self.estado_actual = estadoMotor.estado_7

                    case estadoMotor.estado_7:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_6
                        else:
                            self.estado_actual = estadoMotor.estado_8

                    case estadoMotor.estado_8:
                        if self.z1_direccion:
                            self.estado_actual = estadoMotor.estado_7
                        else:
                            self.estado_actual = estadoMotor.estado_1

            else:
                self.estado_actual = estadoMotor.home

            match self.estado_actual:

                case estadoMotor.home:
                    self.bobina_A = False
                    self.bobina_B = False
                    self.bobina_C = False
                    self.bobina_D = False
            
                case estadoMotor.estado_1:
                    self.bobina_A = False
                    self.bobina_B = False
                    self.bobina_C = True
                    self.bobina_D = True

                case estadoMotor.estado_2:
                    self.bobina_A = False
                    self.bobina_B = False
                    self.bobina_C = True
                    self.bobina_D = False

                case estadoMotor.estado_3:
                    self.bobina_A = False
                    self.bobina_B = True
                    self.bobina_C = True
                    self.bobina_D = False

                case estadoMotor.estado_4:
                    self.bobina_A = False
                    self.bobina_B = True
                    self.bobina_C = False
                    self.bobina_D = False

                case estadoMotor.estado_5:
                    self.bobina_A = True
                    self.bobina_B = True
                    self.bobina_C = False
                    self.bobina_D = False

                case estadoMotor.estado_6:
                    self.bobina_A = True
                    self.bobina_B = False
                    self.bobina_C = False
                    self.bobina_D = False

                case estadoMotor.estado_7:
                    self.bobina_A = True
                    self.bobina_B = False
                    self.bobina_C = False
                    self.bobina_D = True

                case estadoMotor.estado_8:
                    self.bobina_A = False
                    self.bobina_B = False
                    self.bobina_C = False
                    self.bobina_D = True

            time.sleep(0.02)

            if self.electronica:
                self.electronica.Y_03 = self.bobina_A
                self.electronica.Y_04 = self.bobina_B
                self.electronica.Y_05 = self.bobina_C
                self.electronica.Y_06 = self.bobina_D

            print(f" {self.contador} {self.contador * 0.9}º {self.estado_actual} => {self.bobina_A} {self.bobina_B} {self.bobina_C} {self.bobina_D}")
            self.contador +=1

    def establecer_electronica(self, electronica):
        self.electronica = electronica

def main():
    print("Dentro de main")

    mi_motor = MotorPasos()

    electronica = Electronica()
    mi_motor.establecer_electronica(electronica)

    mi_motor.activar_motor()

if __name__== "__main__":
    main()