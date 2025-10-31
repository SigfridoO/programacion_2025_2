import numpy as np
import matplotlib.pyplot as plt

vector_1 = np.arange(0 , 10)
print("Arreglo del 0 al 9: ", vector_1) 

vector_2 = np.array([0 , 10])
print("Arreglo del 0 al 9: ", vector_2) 

matriz = np.array([[1,2], [3,4]])
print("Matriz: \n", matriz)

vector_3 = np.linspace(0 , 10, 10)
print("Arreglo del 0 al 10: ", vector_3) 

vector_4 = np.zeros(8)
print("Vector_4: ", vector_4)

vector_5 = np.zeros(20)
print("vector_5: ", vector_5)


################################### EVALUANDO UNA FUNCION y = 3*x+2 ##############################################

#Ecuación linea recta
'''x = np.linspace(-10, 10, 25)
y = 3*x**2+2

plt.plot(x,y, color = "red", linestyle = "--", marker = 'o')
plt.grid(True)
plt.title("Gráfica de la función")
plt.show()

print("x", x)
print("y", y)'''

#Grafica de barras
'''materias = ["Progra", "Maqui", "SH"]
valores = [20, 60, 90]
plt.bar(materias, valores, color = "blue")
plt.show()'''

#Grafica de pastel
materias = ["Progra", "Maqui", "SH"]
valores = [20, 60, 90]
plt.pie(valores, labels = materias, autopct = "%1.1f%%", colors = ['blue', 'green', 'purple'])
plt.show()

#Varias funciones en una sola grafica
'''pi = 3.1415
tiempo = np.linspace(0, 2*pi, 20)

L1 = np.sin(tiempo)
L2 = np.sin(tiempo-2/3*pi)
L3 = np.sin(tiempo-4/3*pi)

plt.plot(tiempo, L1)
plt.plot(tiempo, L2)
plt.plot(tiempo, L3)
plt.grid(True)
plt.show()'''

'''#Varias subgraficas
fig, axs = plt.subplots(1, 2)

#Primera gráfica
pi = 3.1415
tiempo = np.linspace(0, 2*pi, 20)

L1 = np.sin(tiempo)
L2 = np.sin(tiempo-2/3*pi)
L3 = np.sin(tiempo-4/3*pi)

axs[0].plot(tiempo, L1)
axs[0].plot(tiempo, L2)
axs[0].plot(tiempo, L3)
axs[0].grid(True)

#Segunda grafica
materias =["Progra", "Maqui", "SH"]
valores = [20, 60, 90]
axs[1].bar(materias, valores, color ="red")
plt.show()'''