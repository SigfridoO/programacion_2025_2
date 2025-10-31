#                  CLASE 2:                        FUNDAMENTOS BASICOS
#    VARIABLES

from Varios import nuevoTema , menu, factorial
print(" ")

#  int:
numero = 21
print ("numero:", numero)

#  float:
temperatura = 35.7
print ("temperatura: ", temperatura) 

#str
nombre = "azucarrrrrrrrr"
print ("nombre", nombre)

#bool
eresgymbro = True 
print("eresgymbro: ", eresgymbro)


#       OPERADORES ARITMETIOS
def nuevoTema(OPERADORES_ARITMETICOS):   # Para agregar nuevo tema
 print (f"""///////////////{OPERADORES_ARITMETICOS} ///////////////////
            /////////////////////////////////////////////""")

numero1 = 21
numero2 = 19
#definir
print ("numero1", numero1)
print ("numero2", numero2)
#realizacion de operacion
print ("numero1 + numero2: ", numero1 + numero2) #suma
print ("numero1 - numero2: ", numero1 - numero2) #resta
print ("numero1 / numero2: ", numero1 / numero2) #division
print ("numero1 * numero2: ", numero1 * numero2) #multiplicacion
print ("numero1 % numero2: ", numero1 % numero2) #porcentaje
print ("numero1 ** numero2: ", numero1 ** numero2) #potencia

#       OPERADORES LOGICOS

print (f" {numero1} > {numero2}: {numero1 > numero2}") #mayor que
print (f" {numero1} < {numero2}: {numero1 < numero2}")  #menor que
print (f" {numero1} >= {numero2}: {numero1 >= numero2}") #mayor igual que
print (f" {numero1} <= {numero2}: {numero1 <= numero2}") #menor igual que
print (f" {numero1} == {numero2}: {numero1 == numero2}") #igualdad comparacion


######################## PRIMERA ACTIVIDAD #####################################
#                               LISTAS
nuevoTema("LISTAS")
 
 
print("=======listas=======")
frutas = ["kiwis", "mananas", "melones", "limones", "piñas", "platanos", "naranjas"]
print("frutas: ", frutas)

varios = [23, 457.23, True, "luis", frutas]
print("varios: ", varios)

print("frutas[3]: ", frutas[3])
print("frutas[1:5]: ", frutas[1:5]) #(intervalo del 1 al 5)
print("frutas[1:5:2]: ", frutas[1:5:2]) #(intervalo del 1 al 5 de dos en dos)

print("frutas[:4]: ", frutas[:4]) #(dar objetos del listado del inicio, no especificado, hasta el número 4)
print("frutas[4:]: ", frutas[4:]) #(dar los objetos del listado del 4 al final)

print("tamaño de la lista 'len(frutas)': ", len(frutas))
print("ultimo elemento de la lista 'frutas[len(frutas) - 1]': ", frutas[len(frutas) - 1])
print("ultimo elemento de la lista 'frutas[-1]': ", frutas[-1])
print("penúltimo elemento de la lista 'frutas[-2]': ", frutas[-2])
print("antepenúltimo elemento de la lista 'frutas[-3]:", frutas[-3])

print("agregand un elemento a la lista")
print("frutas.append('mangos'): ", frutas.append('mangos')) #.append es para agregas elementos a listas
print("frutas.append('arandanos'): ", frutas.append('arandanos'))

print("eliminar un elemento a la lista")
print("frutas.remove('kiwis'): ", frutas.remove('kiwis'))
print("frutas: ", frutas)

print("ordenar lista")
print("frutas.sort(): ", frutas.sort())
print("frutas: ", frutas)

print("invertir listas")
print("frutas.reverse(): ", frutas.reverse())
print("frutas: ", frutas)

for i in range(6):
    print(i)

print("-----")

for i in range(3,6):
    print(i)

print("-----")

for i in range(1,20,2):
    print(i)

print("----- con listas")
for fruta in frutas:
        print(fruta)

for indice, fruta in enumerate(frutas):
        print(f"{indice}.-{fruta}")
        
        print("-----For de una sola línea")
        [print(fruta) for fruta in frutas]
        
        print("-----Con en continue")   # Toda esta seccion sirve para que ya no corra el programa 
        for i in range (8):
         if i > 2 and i < 5:
            continue
            print(i)
        
        print(i)
        print("-----Con e El break")   # Toda esta seccion sirve para que ya no corra el programa 
        for i in range (8):
         if i > 2:
            break
        print(i)
        
nuevoTema("while")
menu()

###################  INSTRUCCIONES DE SELECCION ###########################
nuevoTema("INSTRUCCIONES DE SELECCION")

print("Instrucciones de seleccion")
print("---------------if-else")

entrego_proyecto = True
el_proyecto_funciona = True
calificacion = 30
if calificacion >= 70:
    print ("El alumno aprobo :) ")
    
elif entrego_proyecto and el_proyecto_funciona:  ####  elif: es la union de else y if 
      print("Puede que pase")
else:
        print(f"El alumno esta reprobado, su calificación fue: {calificacion} :( ")
        
print("-----Con en continue")   # CONTINUA EL PROGRAMA SE SALTA AL SIGUIENTEFOR
for i in range (8):
         if i > 2 and i < 5:
            continue
            print(i)
        
print(i)
print("-----Con e El break")   # DETIENE EL PROGRAMA (for) FIN
for i in range (8):
         if i > 2:
            break
print(i)   
valor = None
        
if valor:
         print("La condicion es falsa. ")
            
         if not 0:
                print("La condicion es falsa con 0")
                
                if not False:
                 print("La condicion es falsa con False")
                 
                 if not None:
                  print("La condicion es falsa con None")
                 
                 if not []:
                  print("La condicion es falsa con Lista vacia")
                  
############################## FUNCIONES #############################

nuevoTema("FUNCIONES") #Para agregar nuevo tema
print()

numero = -1
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
print()

###################################DICCIONARIOS ############################

nuevoTema("DICCIONARIOS")

persona = {
    'nombre': 'José Luis',
    'Edad': 22,
    'fuma': True,
    'Estatura': 100,
    'Hobbies': {'Tomar', 'leer', 'pintar'}
}
print ('persona: ', persona)
print("...Accediendo a los elemnetos de un diccionario")

print('persona.get("nombre): ', persona.get("nombre"))

print("...Accediendo a las claves")
print('persona.keys():', persona.keys())

print("...Accediendo a los valores")
print('persona.values():', persona.values())

print("...Accediendo a los elementos")
print('persona.items():', persona.items())

print("...Accediendo a la claves valor")
for clave, valor in persona.items():
    print (f"{clave}: {valor}")
