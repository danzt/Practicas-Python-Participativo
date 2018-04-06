"""2)Crea una tupla con valores ya predefinidos del 1 al 10, pide un indice por teclado y muestra los valores de la tupla en cuyo indice."""

#!/usr/bin/python
# -*- coding: utf-8 -*-


lista=range(1,11)
tupla=tuple(lista)

print "Tupla = ", tupla

ind=int(input("Insertar el indice a buscar: " ))


if tupla[ind] in tupla:
	
	print tupla[ind]

else: 
	print "No esta en la tupla"

	








