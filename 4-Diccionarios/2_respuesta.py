"""2)Introducir por teclado una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe  _"que lindo dia que hace hoy"_  debe devolver:  `'que': 2, 'lindo': 1, 'dia': 1, 'hace': 1, 'hoy': 1`."""

#!/usr/bin/python
# -*- coding: utf-8 -*-

dic = []
frecuencia = []

cadena=raw_input("Introducir una cadena: " )
lista = cadena.split(' ')

for i in lista:
	frecuencia.append(lista.count(i))

#print "keys:", lista
#print "values", frecuencia

dic = dict(zip(lista,frecuencia))
print dic


#Referencias:
#https://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python
#https://www.tutorialspoint.com/How-to-create-Python-dictionary-from-list-of-keys-and-values





	















