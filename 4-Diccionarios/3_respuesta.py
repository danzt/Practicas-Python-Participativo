"""3)Crea un diccionario(tipo agenda telefonica) donde la clave sea el nombre del contacto y el valor sea el telefono. Tendras que ir pidiendo ingresar nuevos contactos hasta que el usuario diga que no quiere insertar mas. No se podran meter nombres repetidos, imprimir el diccionario."""


#!/usr/bin/python
# -*- coding: utf-8 -*-
agenda={}
salir ='0'

while True:
	if salir != 's':
		nombre=raw_input("Introduce el nombre: ")
		telefono=int(raw_input("Introduce su telefono: "))
		if nombre not in agenda.keys():
  			agenda[nombre] = telefono
			print "Contacto agendado!"
		else:
			print "Contacto ya ha sido agendado!"

		salir = raw_input("\nPresiona enter para seguir insertando o escribe s para salir-> ")
						
	else:
		print "Agenda: ", agenda
		exit()






