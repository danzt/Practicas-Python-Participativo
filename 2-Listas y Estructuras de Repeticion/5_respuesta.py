#Pedir dos numeros por teclado y validar el tipo de dato de cada variable, si es string pedir nuevamente el ingreso del numero hasta que sea un entero y si es entero realizar una suma de ambos.

#!/usr/bin/python
# -*- coding: utf-8 -*-

while True:
	try:
		x = int(raw_input("Inserte un numero 1: "))
		break
	except ValueError:
		print "Es un string. Inserte un numero valido 1"

while True:
	try:
		y = int(raw_input("Inserte un numero 2: "))
		s=x+y		
		print x+y
		break
	except ValueError:
		print "Es un string. Inserte un numero valido 2"





