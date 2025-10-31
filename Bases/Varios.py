#####################################

def nuevoTema(tema):   # Para agregar nuevo tema
    print(f"##############{tema}###################")
    
def menu():    
    opcion = -1
    
    while not opcion == 0:
    
        print ("____________________________________")
        print ("BIENVENIDO A ESTA TIENDA DE JUGOS")
        print ("____________________________________")
        print ("Elige el jugo que más te guste")
        print ("1. Jugo de naranja")
        print ("2. Jugo de guayaba")
        print ("3. Jugo de zanahoria")
        print ("4. Jugo de fresa")
        print ("0. Salir")
    
        print("Elige una opcion: ")
    
        opcion = int (input())
        print(f"Opcion elegida: {opcion}")
        evaluar_opcion1 (opcion)
    
def evaluar_opcion1(opcion):
    if opcion ==1:
        print("Preparando jugo de naranja")
    elif opcion ==2:
        print("Preparando jugo de guayaba")
    elif opcion ==3:
        print("Preparando jugo de zahanoria")
    elif opcion ==4:
        print("Preparando jugo de fresa")
    else:
    
        pass
    a = input()
    
def evaluar_opcion2 (opcion):
    match opcion:
     case 1:
          print("Preparando jugo de naranja")
     case 2:
           print("Preparando jugo de guayaba")
     case 3:
           print("Preparando jugo de zahanoria")
     case 4:
           print("Preparando jugo de fresa")
     case _:
      pass
a = input()
############################################################
    
def factorial (numero):
    resultado = 1
    if numero < 0:
        return "No se puede calcular el factorial"

    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado