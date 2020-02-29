# Autor: Anayansi Alexia Tafoya Soto, A01746781
# Descripcion: Calcular el porcentaje de hombres y mujeres inscritos en una clase

#Escribe tu programa después de esta línea.
#Leer
mujeres = int (input ("Teclea el número de mujeres inscritas: "))
hombres = int (input ("Teclea el número de hombres inscritos: "))


#Calcular
total = mujeres + hombres
porcentaje1 = (mujeres * 100) / total
porcentaje2 = (hombres * 100) / total

#Imprimir resultados
print ("Total de inscritos: %d" % total)
print ("Porcentaje de mujeres: %.1f" % porcentaje1,"%")
print ("Porcentaje de hombres: %.1f" % porcentaje2,"%")