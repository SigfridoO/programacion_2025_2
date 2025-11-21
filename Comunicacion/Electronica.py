import gpiod
from gpiod.line import Direction, Value
import time
import threading

class Electronica:
    def __init__(self):
        # Entradas Digitales
        self.DI_00 = 14
        self.DI_01 = 15
        self.DI_02 = 18
        self.DI_03 = 23
        self.DI_04 = 24

        # Salidas Digitales
        self.DO_00 = 2
        self.DO_01 = 3
        self.DO_02 = 4
        self.DO_03 = 17
        self.DO_04 = 27
        self.DO_05 = 22
        self.DO_06 = 10
        self.DO_07 = 9

        # Variables virtuales
        self.X_00 = False
        self.X_01 = False
        self.X_02 = False
        self.X_03 = False
        self.X_04 = False

        self.Y_00 = False
        self.Y_01 = False
        self.Y_02 = False
        self.Y_03 = False
        self.Y_04 = False
        self.Y_05 = False
        self.Y_06 = False
        self.Y_07 = False

        # configurando pines
        self.chip = gpiod.Chip("/dev/gpiochip0")
        self.request = self.chip.request_lines(
            consumer="prueba led",
            config={
                # Entradas Digitales
                self.DI_00: gpiod.LineSettings(direction= Direction.INPUT),
                self.DI_01: gpiod.LineSettings(direction= Direction.INPUT),
                self.DI_02: gpiod.LineSettings(direction= Direction.INPUT),
                self.DI_03: gpiod.LineSettings(direction= Direction.INPUT),
                self.DI_04: gpiod.LineSettings(direction= Direction.INPUT),

                #Salidas Digital
                self.DO_00 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_01 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_02 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_03 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_04 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_05 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_06 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_07 : gpiod.LineSettings(direction = Direction.OUTPUT, output_value=Value.INACTIVE),
            }
        )

        self.funcionando_pines = False
        self.tarea = threading.Thread(target= self.iniciar)
        self.tarea.start()


    def iniciar(self):
        self.funcionando_pines = True
        while self.funcionando_pines:
            # Mapeo de variables
            self.X_00 = True if self.request.get_value(self.DI_00) == Value.ACTIVE else False
            self.X_01 = True if self.request.get_value(self.DI_01) == Value.ACTIVE else False
            self.X_02 = True if self.request.get_value(self.DI_02) == Value.ACTIVE else False
            self.X_03 = True if self.request.get_value(self.DI_03) == Value.ACTIVE else False
            self.X_04 = True if self.request.get_value(self.DI_04) == Value.ACTIVE else False

            self.request.set_value(self.DO_00, Value.ACTIVE if self.Y_00 == True else Value.INACTIVE)
            self.request.set_value(self.DO_01, Value.ACTIVE if self.Y_01 == True else Value.INACTIVE)
            self.request.set_value(self.DO_02, Value.ACTIVE if self.Y_02 == True else Value.INACTIVE)
            self.request.set_value(self.DO_03, Value.ACTIVE if self.Y_03 == True else Value.INACTIVE)

            self.request.set_value(self.DO_04, Value.ACTIVE if self.Y_04 == True else Value.INACTIVE)
            self.request.set_value(self.DO_05, Value.ACTIVE if self.Y_05 == True else Value.INACTIVE)
            self.request.set_value(self.DO_06, Value.ACTIVE if self.Y_06 == True else Value.INACTIVE)
            self.request.set_value(self.DO_07, Value.ACTIVE if self.Y_07 == True else Value.INACTIVE)
            time.sleep(0.001)
            # Programa
            #Y_00 = (X_00 or Y_00) and not X_01


    def cerrar(self):
        self.request.release()
        self.chip.close()

