#Ingresar Datos a un lista por consola
lista=[]

op = 1

while op > 0:
	
	print "Menu:"
	print "1) Ingresar un valor entero a la lista"
	print "2) Eliminar un valor de la lista"
	print "3) Mostrar Lista"
	print "0) Salir"

	op = int(input("Ingrese una opcion: "))

	if op == 1:
		val = int(input("Ingrese un valor entero: "))

		if val in lista:
			print "Ya existe ese valor"
		else :
			lista.append(val)

	elif op == 2:
		val = int(input("Ingrese un valor entero a eliminar: "))

		if val in lista:
			lista.remove(val)
			print "Eliminado"
		else :
			print "El valor no existe en la lista"

	elif op == 3:
		print "Lista Ingresada : {}".format(lista)

	elif op == 0:
		print "Programa Terminado"
	
	else :
		print "Ingrese una opcion valida!!"