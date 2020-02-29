#Autor: Anayansi Alexia Tafoya Soto, A01746781
#Descripción: Calcular los ingredientes necesarios para la
#elaboración de galletas.

#Leer
galletas = int (input("Teclea la cantidad de galletas que deseas elaborar: "))

#Calcular
azúcar = (galletas * 1.5) /48
mantequilla = (galletas * 1) /48
harina = (galletas * 2.75) / 48

#Imprimir
print ("La cantidad de azúcar necesaria es de: %.2f tazas" % azúcar)
print ("La cantidad de mantequilla necesaria es de: %.2f tazas" % mantequilla)
print ("La cantidad de harina necesaria es de: %.2f tazas" % harina)