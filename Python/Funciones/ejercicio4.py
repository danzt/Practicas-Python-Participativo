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
	for x in xrange(0,number/2):
		print '*'

def down(number):
	up(number)
	i = (number/2)

	for x in xrange(i,number):
		print '*'


def index(number):
	down(number)
	
number = input("Ingrese el ancho del triangulo para dibujar: ")
index(number)