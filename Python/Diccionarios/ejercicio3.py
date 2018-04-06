# -*- coding: utf-8 -*-
#3)Crea un diccionario(tipo agenda telefonica) donde la clave sea el nombre del contacto y el valor 
#sea el teléfono. Tendrás que ir pidiendo ingresar nuevos contactos hasta que el usuario diga que no 
#quiere insertar mas. No se podrán meter nombres repetidos, imprimir el diccionario.

print "Agenda Telefonica"

op = 4

dic = {}

while op > 0:
	print "1: Ingresar un nuevo contacto"
	print "2: Mostrar contactos"
	print "0: Finalizar sistema"
	op = input('Ingrese una opcion: ')

	if op == 1:
		name = input('Ingrese el nombre del contacto: ')
		tlf = input('Ingrese el telefono: ')
		if name in dic:
			print 'Error!! ya ese contacto existe'
		else :
			dic[name] = tlf
			print 'Usuario Agregado'
	if op == 2:
		print 'Lista de contactos:'
		print dic