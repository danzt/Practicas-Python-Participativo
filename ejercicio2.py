# -*- coding: utf-8 -*-
#2) Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.

a = int(input("Ingrese un numero Entero: "))

b = int(input("Ingrese otro numero Entero: "))

if a%b == 0:
	print ("La division es exacta")
else :
	print ("la division no es exacta")