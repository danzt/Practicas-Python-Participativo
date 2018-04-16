"""4)Ingresar el ancho de un triangulo y apartir del ancho se dibuje el triangulo con (*), hacerlo con funciones, una funcion que rellene la parte de arriba y otra la parte de abajo, ademas, hacer una funcion index para recibir los datos por teclado y llamar a las demas funciones dentro de ella."""


#!/usr/bin/python
# -*- coding: utf-8 -*-

def index():
	ancho=int(input('Inserte el ancho del triangulo: '))
	arriba_triangulo(ancho)
	abajo_triangulo(ancho)

def arriba_triangulo(ancho):
	for i in range(1, ancho, 1):
		print i*"*"

def abajo_triangulo(ancho):
	for i in range(ancho, 0, -1):
		print i*"*"

index()
