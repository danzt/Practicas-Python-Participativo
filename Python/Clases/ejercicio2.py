# -*- coding: utf-8 -*-
"""
2)crear una clase llamada persona, que va a tener como atributos "nombre" y "edad", con dos métodos, uno para obtener 
el nombre (que lo imprima por pantalla) y otro para obtener la edad, y después una clase llamada alumno, que aparte de 
tener una edad y un nombre como la clase persona, también va a tener el atributo "nota" con un método para obtener la 
nota... usar herencia...
"""

class Persona(object):
	"""docstring for Persona"""
	def __init__(self):
		self.__name = None
		self.__age = None

	def name(self, name):
		self.__name = name

	def printName(self):
		print "Nombre: {}".format(self.__name)

	def age(self, age):
		self.__age = age

	def printAge(self):		
		print "Edad: {}".format(self.__age)

class Alumno(Persona):
	"""docstring for Alumno"""
	def __init__(self):
		#super(Persona, self).__init__()
		self.__score = None

	def score(self, score):
		self.__score = score

	def printStudent(self):
		print "Alumno Ingresado:"
		self.printName()
		self.printAge()
		print "Nota: {}".format(self.__score)

def main():
	student =  Alumno()
	student.name(input("Ingrese Nombre del Alumno: "))
	student.age(input("Ingrese Edad del Alumno: "))
	student.score(input("Ingrese Nota del Alumno: "))
	student.printStudent()

main()