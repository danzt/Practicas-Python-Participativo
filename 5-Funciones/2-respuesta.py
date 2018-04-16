"""2)Definir una funcion que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la funcion len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio."""


#!/usr/bin/python
# -*- coding: utf-8 -*-


lista=[1,11,8,6,4,3,7,2,14,9] 
cadena="Hoy voy a caminar"

def long_lista(lista):
	print lista, 'la longitud es: ',len(lista)

def long_cadena(cadena):
	print cadena, 'la longitud es' ,len(cadena)

long_lista(lista)
long_cadena(cadena)
