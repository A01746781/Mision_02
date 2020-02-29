# Autor: Anayansi Alexia Tafoya Soto, A01746781
# Descripcion: Calcular el costo total de ua comida en un restaurante con propina e IVA incluida.

# Escribe tu programa después de esta línea.

#Leer
subtotal = int (input("Teclea el total de tu comida: "))

#Calcular
propina = subtotal * 0.13
IVA = subtotal * 0.16
total = subtotal + propina + IVA

#Imprimir
print ("Costo de su comida: %d" % subtotal)
print ("Propina: $%.2f" % propina)
print ("IVA: $%.2f" % IVA)
print ("Total a pagar: $%.2f" % total)