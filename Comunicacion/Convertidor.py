from struct import pack, unpack

class Convertidor:
    def __init__(self):
        self.cadena = bytearray(25)
        self.indice = 0

    def generar_mensaje(self, tipo_instruccion, num_instruccion, args = []):
        self.indice = 0
        self.agregar_caracteres("*")
        self.agregar_entero1(tipo_instruccion + 48)
        self.agregar_entero1(num_instruccion + 48)
        
        if args and isinstance(args, list):
            for item in args:
                self.agregar_entero1(item +48 )

        self.agregar_caracteres("_")
        return self.cadena[0: self.indice]

    def agregar_entero1(self, numero:int):
        arreglo = pack('B', numero)
        self.agregar_bytes(arreglo)

    def agregar_caracteres(self, texto):
        arreglo = texto.encode('ascii')
        self.agregar_bytes(arreglo)

    def agregar_bytes(self, arreglo:bytes):
        for i , elemento in enumerate(arreglo):
            self.cadena[self.indice] = arreglo[i]
            self.indice = self.indice + 1

def main():
    convertidor = Convertidor()
    mensaje = convertidor.generar_mensaje(1, 3, [2, 1])
    print("mensaje: ", mensaje)

if __name__=='__main__':
    main()