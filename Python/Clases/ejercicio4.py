# -*- coding: utf-8 -*-
"""
4)Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones:
-   Añadir contacto
-   Lista de contactos
-   Buscar contacto
-   Editar contacto
-   Cerrar agenda
"""

class diary(object):
	"""docstring for diary"""
	def __init__(self):
		self.arg = None
		self.__contact = {}

	def newContact(self,name,phone,email):
		self.__contact[name] = [name,phone,email]
		return "Contacto Guardado"

	def printContact(self):
		return self.__contact.values()

	def search(self,name):
		if self.__contact.get(name) == None:
		 	return ">>>>Contacto No Registrado!!<<<<"
		else:
			return self.__contact[name]

	def edit(self,name):
		if self.__contact.get(name) == None:
		 	return ">>>>Contacto No Registrado!!<<<<"
		else:
			print "Contacto a editar: {}".format(self.__contact[name])
			print "1) Nombre"
			print "2) Telefono"
			print "3) Correo"
			op = input('Opcion a editar: ')

			if op < 1 or op > 3:
				return ">>>>ERROR!! Opcion Incorecta!<<<<"
			else:
				edit = input('Nuevo Dato: ')
				self.__contact[name][op-1]= edit
				return "Contacto Editado"

def main():
	op = 1
	contact = diary()

	while op != 5:
		print "------Agenda------"
		print "1) Añadir contacto"
		print "2) Lista de contactos"
		print "3) Buscar contacto"
		print "4) Editar contacto"
		print "5) Cerrar agenda"
		op = input("Ingrese una opcion: ")

		if op == 1:
			print "------Nuevo Contacto------"
			name = input('Ingrese Nombre: ')
			phone = input('Ingrese Telefono: ')
			email = input('Ingrese Correo: ')

			print contact.newContact(name,phone,email)
		elif op == 2:
			print contact.printContact()
		elif op == 3:
			name = input('Ingrese Nombre: ')
			print contact.search(name)
		elif op == 4:
			name = input('Ingrese Nombre: ')
			print contact.edit(name)
		elif op == 5:
			print "<<<<Adios!>>>>"
		else:
			print "<<<<Error! Opcion Invalida!>>>>"

main()
	
