# -*- coding: utf-8 -*-
#3)ingresar una fecha por teclado que cumpla con este formato(Día, Mes, Año) (donde Día, Mes y Año son números 
#enteros) calcule el día siguiente al dado, en el mismo formato e imprimir ambas tuplas 'fecha ingresada' y 
#'fecha del dia siguiente'!
print "Ingrese una fecha"

a = input("Dia en valor numerico: ")
b = input("Mes en valor numerico: ")
c = input("Anio en valor numerico: ")

centinel = True

while centinel:
	centinelA = False
	centinelB = False
	centinelC = False

 	if type(a) is int:
		if (a < 1 or a > 31):
			a = input("ERROR!!! El rango de dias es entre 1 y 31: ")
		else:
			centinelA = True
	else:
		a = input("ERROR!!! Solo Valores numericos para dias: ")

	if type(b) is int:
		if b < 1 or b > 12:
			b = input("ERROR!!! El rango de meses es entre 1 y 12: ")
		else:
			centinelB = True
	else:
		b = input("ERROR!!! Solo Valores numericos para meses: ")	

	if type(c) is int:
		if c < 1:
			c = input("ERROR!!! El anio debe ser mayor que 0: ")
		else:
			centinelC = True
	else:
		c = input("ERROR!!! Solo Valores numericos para anio: ")	

	if centinelA and centinelB and centinelC:
		centinel = False

dateI = a,b,c
print "Fecha ingresada: {}".format(dateI)

if a >= 31:
	a = 1
	if b >= 12:
		b = 1
		c = c + 1
	else:
		b = b + 1
else:
	a = a + 1

dateN = a,b,c
print "Fecha del dia siguiente: {}".format(dateN)