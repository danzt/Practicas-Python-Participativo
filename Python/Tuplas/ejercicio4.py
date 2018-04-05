# -*- coding: utf-8 -*-
#4)ingresar una fecha por teclado que cumpla con este formato(Día, Mes, Año) (donde Día y Año son números 
#enteros y Mes es un string 'enero','febrero'...) calcule el día siguiente al dado, en el mismo formato e 
#imprimir ambas tuplas 'fecha ingresada' y 'fecha del dia siguiente'.

print "Ingrese una fecha"

a = input("Dia en valor numerico: ")
b = input("Mes en texto('Mes'): ")
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

	if type(b) is str:
		centinelB = True
	else:
		b = input("ERROR!!! Solo texto para meses (ejemplo 'Febrero'): ")	

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
	if b.upper() == 'DICIEMBRE':
		b = 'Enero'
		c = c + 1
else:
	a = a + 1

dateN = a,b,c
print "Fecha del dia siguiente: {}".format(dateN)