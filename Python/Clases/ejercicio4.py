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

def main():
	op = 1
	while op != 5:
		print "Agenda"
		print "1) Añadir contacto"
		print "2) Lista de contactos"
		print "3) Buscar contacto"
		print "4) Editar contacto"
		print "5) Cerrar agenda"
		op = input("Ingrese una opcion: ")

		if op == 1:
			pass
		elif op == 2:
			pass
		elif op == 3:
			pass
		elif op == 4:
			pass
		elif op == 5:
			print "Adios!"
		else:
			print "Error! Opcion Invalida!"

main()
	
