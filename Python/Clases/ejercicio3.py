# -*- coding: utf-8 -*-
"""
3)Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular 
después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
"""

class Calculadora(object):
	"""docstring for Calculadora"""
	def __init__(self, a = 0, b = 0):
		self.__a = a
		self.__b = b

	def sum(self):
		print "la suma es: {}".format(self.__a  + self.__b)
	
	def subs(self):
		print "la resta es: {}".format(self.__a  - self.__b)

	def mul(self):
		print "la multiplicación es: {}".format(self.__a  * self.__b)

	def div(self):
		if self.__b == 0:
			print "División entre cero(0) no valida"
		else:
			print "la división es: {}".format(self.__a  / self.__b)

def main():
	a = input("Ingrese un valor enterto: ")
	b = input("Ingrese segundo valor enterto: ")
	calculator = Calculadora(a,b)
	calculator.sum()
	calculator.subs()
	calculator.mul()
	calculator.div()

main()