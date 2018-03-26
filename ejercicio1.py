# -*- coding: utf-8 -*-
#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.
#(investigar como introducir datos por teclado)

a = float(input("Ingrese un valor numerico(Si es decimal separarlos con . ejm 1.1): "))

b = float(input("Ingrese un segundo valor numerico(Si es decimal separarlos con . ejm 1.1): "))

if a > b :
	print ("El valor", a ,"es mayor que", b)
elif b > a :
	print ("El valor", a ,"es menor que", b)
else :
	print ("Los valores son Iguales")