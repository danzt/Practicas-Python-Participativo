"""2)Definir una funcion que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la funcion len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio."""

#!/usr/bin/python
# -*- coding: utf-8 -*-

lista=[1,11,8,6,4,3,7,2,14,9] 
cadena="Hoy voy a caminar"

def long_lista(lista):
	count = 0
	for i in lista:
		count = count+1
	
	print lista, 'la longitud es: ', count

def long_cadena(cadena):
	count = 0
	for i in cadena:
		count = count+1
	
	print cadena, 'la longitud es: ', count


long_lista(lista)
long_cadena(cadena)


#NOTA: Si la entrada es por la consola el manejo seria con una sola funcion
