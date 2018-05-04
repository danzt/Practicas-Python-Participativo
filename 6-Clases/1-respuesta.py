"""1)Escribir una clase en python llamada **rectangulo** que contenga una base y una altura, y que contenga un metodo que devuelva el area del rectangulo."""

#!/usr/bin/python
# -*- coding: utf-8 -*-

class Rectangulo:

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura
		print 'Se creo el rectangulo'
		
	def area_rectangulo(self):
		area = self.base * self.altura
		print 'El area es: ', area


recta = Rectangulo(5,5)
recta.area_rectangulo()

