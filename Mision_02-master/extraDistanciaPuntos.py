#Autor: Anayansi Alexia Tafoya Soto, A01746781
#Descripción: Este programa calcula la distancia entre dos puntos.

#Leer
c1 = int (input("Teclea las coordenadas x1: "))
c2 = int (input("Teclea las coordenadas y1: "))
c3 = int (input("Teclea las coordenadas x2: "))
c4 = int (input("Teclea las coordenadas y2: "))

#Calcular
import math
distancia = (c3-c1)**2 + (c4-c2)**2
r = math.sqrt (distancia)

#Imprimir
print ("Distancia: %.3f" % r )