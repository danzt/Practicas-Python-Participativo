"""4)Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el telefono y el email. Ademas debera mostrar un menu con las siguientes opciones
-   Anadir contacto
-   Lista de contactos
-   Buscar contacto
-   Editar contacto
-   Cerrar agenda
"""

# coding: utf-8
#!/usr/bin/python

lista=[]
class Agenda(object):
	def __init__(self):
		self.nombre = None
		self.telefono = None
		self.email=None 		
		self.agenda={}

	def Contactos(self):
		if self.nombre not in self.agenda.keys():
			lista = [self.telefono, self.email]
			self.agenda = {self.nombre: lista}
			print "\nContacto agregado!\n"
		else:
			print "\nYa existe\n"
			
	def Listar(self):
		print 'Listado:'
		print self.agenda
		
	def Buscar(self, nombre):
		print self.agenda.get(self.nombre)
		print '\n'

	def Editar(self, nombre):
		if self.nombre in self.agenda.keys():
			lista = [self.telefono, self.email]
			self.agenda = {self.nombre: lista}
			print '\nContacto anterior: ', self.agenda.get(self.nombre)
			print '\nContacto modificado!', self.agenda.get(self.nombre)

		
	def Cerrar(self):
		exit()

A=Agenda()

while True:
	print '\n###########################################\n'
	print '\n 0 Anadir contacto\n 1 Lista de contactos\n 2 Buscar contacto\n 3 Editar contacto\n 4 Cerrar agenda\n'
	print '\n###########################################\n'

	opcion = raw_input("Seleccione la opcion a realizar: ")
	if (opcion == '0'):
		A.nombre =raw_input("Introduce el nombre: ")
		A.telefono=int(raw_input("Introduce su telefono: "))
		A.email=raw_input("Introduce su email: ")
		A.Contactos()
		
	elif (opcion =='1'):
		A.Listar()

	elif (opcion =='2'):
		nombre=raw_input("Inserte el nombre a buscar: ")
		A.Buscar(nombre)
	
	elif (opcion =='3'):
		print 'Este metodo edita el telefono y email'
		nombre=raw_input("Inserte el nombre a buscar: ")
		A.telefono=int(raw_input("Introduce su telefono: "))
		A.email=raw_input("Introduce su email: ")
		A.Editar(nombre)
		
	elif (opcion =='4'):
		A.Cerrar()

	else:
		print ('Seleccione una opcion valida!!!')



