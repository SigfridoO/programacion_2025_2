import time 
import threading
from Temporizador import Temporizador
from PuertoSerie import PuertoSerie
from Convertidor import Convertidor


class Control:
    def __init__(self):
        print("Dentro de Control")
        self.control_funcionando =False
        self.TON_0 = Temporizador("TON_00", 1)
        self.contador = 0
        self.tarea = threading.Thread(target=self.iniciar_control)

        self.numero_de_X = 10
        self.X = []
        for i in range (self.numero_de_X):
            self.X.append (False)

        self.numero_de_Y = 10
        self.Y = []
        for i in range (self.numero_de_Y):
            self.Y.append (False)
              
        self.numero_de_M = 10
        self.M = []
        for i in range (self.numero_de_M):
            self.M.append (False)


        self.numero_de_ESP_X = 10
        self.ESP_X = []
        for i in range (self.numero_de_ESP_X):
            self.ESP_X.append(False)

        self.puerto_serie = PuertoSerie()
        self.puerto_serie.establecer_control(self)

        self.worker = None

        self.convertidor = Convertidor()


    def iniciar_comunicacion(self):
        self.puerto_serie.puerto_serie.open()

    def terminar_comunicacion(self):
        self.puerto_serie.puerto_serie.close()

    def activar_senal_esp32(self, indice, estado):
        mensaje = self.convertidor.generar_mensaje(1, 3, [indice, estado])
        print (f"El mensaje a enviar es {mensaje}")
        respuesta = self.puerto_serie.enviar_mensaje(mensaje)

    def establecer_worker(self, worker):
        self.worker = worker 
        

    def iniciar_puerto_serie(self):
        self.tarea2 =threading.Thread(target= self.puerto_serie.prueba_lectura )
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
                self.Y[0] = not self.Y[0]
                self.Y[1] = not self.Y[1]
                self.Y[2] = not self.Y[2]
                #self.Y[0] = self.ESP_X[3]
                print("Y[0]: ", self.Y[0])
                if self.worker:
                    self.worker.prender_indicador_rojo(self.Y[0])
                    self.worker.prender_indicador_amarillo(self.Y[1])
                    self.worker.prender_indicador_verde(self.Y[2])

            time.sleep(0.001)



def main():
    print("Dentro de main")
    control = Control()
    control.iniciar()


if __name__ == "__main__":
    main()