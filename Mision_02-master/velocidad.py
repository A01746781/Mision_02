# Autor: Anayansi Alexia Tafoya Soto, A01746781
# Descripcion: Calcular las diferentes distancias y tiempo estimados.

# Escribe tu programa después de esta línea.

velocidad= int (input("Teclea la velocidad a la que viaja el auto en km/h (enteros): "))

#Calcular
d1= (velocidad*6)
d2= (velocidad*3.5)
t= (485/velocidad)

#Imprimir
print ("La velocidad de auto en km/h: %d" % velocidad)
print ("La distancia en km. que recorre en 6hrs son: %.1f km" % d1)
print ("La distancia en km. que recorre en 3.5 hrs son: %.1f km" % d2 )
print ("El tiempo en horas que requiere para recorrer 485 km. es de: %.1f hrs." % t)