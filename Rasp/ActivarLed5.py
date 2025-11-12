import gpiod
from gpiod.line import Direction, Value
import time

# Salida digital
LED_PIN = 17

# configurando pines
chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer="prueba led",
    config={
        #Salida Digital
        LED_PIN : gpiod.LineSettings(direction = Direction.OUTPUT, 
                                    output_value=Value.INACTIVE)
    }
)
try:
    while True:
        # Mapeo de variables
        request.set_value(LED_PIN, Value.INACTIVE)
        time.sleep(1)
        request.set_value(LED_PIN, Value.ACTIVE)
        time.sleep(1)
except KeyboardInterrupt:
    print("El usuario termino el programa")
finally:
    request.release()
    chip.close()

