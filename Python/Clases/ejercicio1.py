# -*- coding: utf-8 -*-
"""
1)Escribir una clase en python llamada **rectangulo** que contenga una base y una altura, y que contenga un método 
que devuelva el área del rectángulo.
"""

class rectangulo:
	"""docstring for rectangulo"""
	def __init__(self):
		self.__base = 0
		self.__height = 0
	
	def base(self, base):
		self.__base = base

	def height(self,height):
		self.__height = height

	def area(self):
		print "El Area del Rectangulo es: {}".format((self.__base * self.__height))

def main():
	Area = rectangulo()
	Area.base(input("Ingrese Base de un rectangulo: "))
	Area.height(input("Ingrese Altura de un rectangulo: "))
	Area.area()

main()