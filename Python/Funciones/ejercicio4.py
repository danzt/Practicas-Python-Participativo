# -*- coding: utf-8 -*-
"""4)Ingresar el ancho de un triangulo y apartir del ancho se dibuje el triangulo con (*), hacerlo con funciones, una funcion 
que rellene la parte de arriba y otra la parte de abajo, ademas, hacer una funcion index para recibir los datos por teclado y 
llamar a las demas funciones dentro de ella.
figura ejemplo:
*
**
***
****
*****
****
***
**
*"""

def up(number):
	a = '*'
	print a
	for x in xrange(1,number):
		a = a + '*'
		print a
	return a
		

def down(number):
	a = up(number)
	for x in xrange(1,number):
		print a[::x]


def index():
	number = input("Ingrese el ancho del triangulo para dibujar: ")
	down(number)
	
index()