#Ingresar tuplas a un lista por consola
lista=[]

op = 1

while op > 0:
	
	print "Menu:"
	print "1) Ingresar un alumno a la lista"
	print "2) Eliminar un valor de la lista"
	print "3) Mostrar Lista"
	print "0) Salir"

	op = int(input("Ingrese una opcion: "))

	if op == 1:
		repetido = ""
		a = int(input("Ingrese un valor entero: "))
		b = input("Ingrese nombre: ")
		c = input("Ingrese apellido: ")

		val = a,b,c


		if len(lista) > 0:
			for x in lista:
				if x[0] == a:
					print "Ya existe alumno con ese valor"
					repetido = "true"
					break

			if not repetido :
				lista.append(val)
				print "Agregado."

		else:
			lista.append(val)
			print "Agregado"

	elif op == 2:
		repetido = ""
		a = int(input("Ingrese un valor entero: "))

		if len(lista) > 0:
			for x in lista:
				val = x
				
				if x[0] == a:
					lista.remove(val)
					repetido = "true"
					break

			if repetido :
				print "Eliminado"

		else:
			print "Lista Vacia"

	elif op == 3:
		print "Lista Ingresada : {}".format(lista)

	elif op == 0:
		print "Programa Terminado"
	
	else :
		print "Ingrese una opcion valida!!"