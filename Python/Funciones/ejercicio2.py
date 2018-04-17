# -*- coding: utf-8 -*-
"""2)Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio."""

def new_len(list):
	count = 0

	for x in list:
		count = count +1

	return count

a = input("Ingrese una cadena o una lista: ")

print "longitud de la cadena o lista: {}".format(new_len(a))