import time
import serial


class PuertoSerie:
    def __init__(self):
        print("Dentro de puerto Serie")
        self.puerto_serie = serial.Serial()
        self.puerto_serie.port = "/dev/ttyUSB0"
        self.puerto_serie.baudrate = 115200
        self.puerto_serie.parity = serial.PARITY_NONE
        self.puerto_serie.timeout = 1
        self.puerto_serie.stopbits = serial.STOPBITS_ONE
        self.puerto_serie.bytesize = serial.EIGHTBITS
        
        self.control = None
    
    def establecer_control(self, control):
        self.control = control
        
    def prueba_lectura(self):
        print("--- Iniciando prueba ---")
        
        self.puerto_serie.open()
        if self.puerto_serie.is_open:
            while True:
                r = self.puerto_serie.read(1)
                if r is not None and len(r) > 0:
                    print(f"r: {r}")
                    if self.control:
                        self.control.Esp_x[2] = r[0] - 48
def main():
    print("Dentro de main")
    puerto_serie = PuertoSerie()
    puerto_serie.prueba_lectura()

if __name__ == "__main__":
    main()