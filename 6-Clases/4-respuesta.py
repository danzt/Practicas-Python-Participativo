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
agenda_contacto={}
agenda_persona={}
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
			return self.agenda
		else:					
			print "\nYa existe\n"	
		
	def Agendar(self, agenda_de_persona):
		agenda_contacto.update(agenda_de_persona)
		return agenda_contacto

	def Listar(self, agenda_de_contactos):
		print '\nListado:\n'
		print agenda_de_contactos
		
	def Buscar(self, nombre):
		if self.nombre in self.agenda.keys():
			print self.agenda.get(self.nombre)
			print '\n'
		else:
			print '\nContacto no encontrado!!!\n'

	def Editar(self, nombre):
		if self.nombre in self.agenda.keys():
			del(agenda_contacto[nombre])
			lista = [self.telefono, self.email]
			self.agenda = {self.nombre: lista}
			print '\nContacto Modificado!!!\n'
			return self.agenda
		else:
			print '\nContacto no encontrado!!!\n'
		
	def Cerrar(self):
		exit()

A=Agenda()
Agenda_Persona={}
Agenda_Contacto={}
Contacto_modificado={}

while True:
	print '\n###########################################\n'
	print '\n 0 Anadir contacto\n 1 Lista de contactos\n 2 Buscar contacto\n 3 Editar contacto\n 4 Cerrar agenda\n'
	print '\n###########################################\n'

	opcion = raw_input("Seleccione la opcion a realizar: ")
	if (opcion == '0'):
		A.nombre =raw_input("Introduce el nombre: ")
		A.telefono=int(raw_input("Introduce su telefono: "))
		A.email=raw_input("Introduce su email: ")
		Agenda_Persona = A.Contactos()
		Agenda_Contacto = A.Agendar(Agenda_Persona)
		
	elif (opcion =='1'):
		A.Listar(Agenda_Contacto)

	elif (opcion =='2'):
		nombre=raw_input("Inserte el nombre a buscar: ")
		A.Buscar(nombre)
	
	elif (opcion =='3'):
		
		print '\nEste metodo edita el telefono y email\n'
		nombre=raw_input("Inserte el nombre a buscar: ")
		print '\nSu contacto es: ', nombre
		A.Buscar(nombre) 
		A.telefono=int(raw_input("Introduce telefono nuevo: "))
		A.email=raw_input("Introduce su email nuevo: ")
		Contacto_modificado = A.Editar(nombre)
		Agenda_Contacto = A.Agendar(Contacto_modificado)

	elif (opcion =='4'):
		A.Cerrar()

	else:
		print ('Seleccione una opcion valida!!!')



