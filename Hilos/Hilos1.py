import time
import threading



class Tarea:
    def __init__(self, Nombre, Duracion):
        
        self.nombre = Nombre
        self.duracion = Duracion
        
        self.tarea = threading.Thread(target=self.iniciar_tarea)
        
    def iniciar_tarea(self):
        print(f"----Iniciando la tarea {self.nombre}")
        time.sleep(self.duracion)
        print(f"----Terminando la tarea {self.nombre}")
        
    def iniciar(self):
        self.tarea.start()
        
def main():
    print("Dentro de main")
    
    tarea1 = Tarea("Construccion de la estructura", 5)
    tarea1.iniciar()
    
    tarea2 = Tarea("Programacion de RASPBERRY con ESP32 y WIFI", 6)
    tarea2.iniciar()
    
    tarea3 = Tarea("Adquisicion de materiales", 4)
    tarea3.iniciar()
    
if __name__ == "__main__":
    main()