# -*- coding: utf-8 -*-
# 4)Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

a = int(input("Ingrese un numero entero: "))

b = int(input("Ingrese otro numero entero: "))

if a > b:
	if a%b == 0:
		print "{} es multiplo de {}".format(a,b)
	else:
		print "{} NO es multiplo de {}".format(a,b)
elif a < b:
	if b%a == 0:
		print "{} es multiplo de {}".format(b,a)
	else:
		print "{} No es multiplo de {}".format(b,a)
else:
	print "Son iguales"