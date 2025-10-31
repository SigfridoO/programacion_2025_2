import time
import threading
from Temporizador import Temporizador
from PuertoSerie import PuertoSerie


class Control:
    def __init__(self):
        print("Dentro de control")
        self.control_funcionando = False
        self.TON_0 = Temporizador("TON_00", 1)
        self.contador = 0
        self.tarea = threading.Thread(target=self.iniciar_control)
        
        self.numero_de_X = 10
        self.X = []
        for i in range(self.numero_de_X):
            self.X.append(False)
        
        self.numero_de_Y = 10
        self.Y = []
        for i in range(self.numero_de_Y):
            self.Y.append(False)
            
        self.numero_de_M = 10
        self.M = []
        for i in range(self.numero_de_M):
            self.M.append(False)
            
        self.numero_de_Esp_x = 10
        self.Esp_x = []
        for i in range(self.numero_de_Esp_x):
            self.Esp_x.append(False)
            
        self.puerto_serie = PuertoSerie()
        self.puerto_serie.establecer_control(self)
        
    def inicia_puerto_serie(self):
        self.tarea2 = threading.Thread(target=self.puerto_serie.prueba_lectura)
        self.tarea2.start()
        
    def iniciar(self):
        self.tarea.start()
        
    def iniciar_control(self):
        self.control_funcionando = True
        while self.control_funcionando:
            self.TON_0.entrada = not self.TON_0.salida
            self.TON_0.actualizar()
            
            if self.TON_0.salida:
                #self.contador += 1
                #print(self.contador)
                #self.Y[0] = not self.Y[0]
                self.Y[0] = self.Esp_x[2]
                print("Y[0]: ", self.Y[0])
            
            time.sleep(0.001)
        
def main():
    print("Dentro de main")
    control = Control()
    control.iniciar()
    
if __name__ == "__main__":
    main()