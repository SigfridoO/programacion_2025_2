import gpiod
from gpiod.line import Direction, Value
import time

# Entrada Digital
DI_00 = 14
DI_01 = 15

# Salida digital
DO_00 = 17

# Variables virtuales
X_00 = False
X_01 = False

Y_00 = False

# configurando pines
chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer="prueba led",
    config={
        # Entradas Digitales
        DI_00: gpiod.LineSettings(direction= Direction.INPUT),
        DI_01: gpiod.LineSettings(direction= Direction.INPUT),

        #Salida Digital
        DO_00 : gpiod.LineSettings(direction = Direction.OUTPUT, 
                                    output_value=Value.INACTIVE)
    }
)
try:
    while True:
        # Mapeo de variables
        X_00 = True if request.get_value(DI_00) == Value.ACTIVE else False
        X_01 = True if request.get_value(DI_01) == Value.ACTIVE else False

        request.set_value(DO_00, Value.ACTIVE if Y_00 == True else Value.INACTIVE)

        # Programa
        Y_00 = (X_00 or Y_00) and not X_01


except KeyboardInterrupt:
    print("El usuario termino el programa")
finally:
    request.release()
    chip.close()

