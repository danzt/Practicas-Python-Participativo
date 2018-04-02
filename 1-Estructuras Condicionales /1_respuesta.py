"""1) Escriba un programa que pida dos numeros y que conteste cual es el menor y cual es el mayor o que escriba que son iguales (Investigar como instroducir los datos por teclado)"""

# coding: utf-8
#!/usr/bin/python

"""Insertar datos al programa"""
num1=raw_input("Inserte un numero 1: ")
num2=raw_input("Inserte un numero 2: ")
	
if num1 > num2:
	print "El mayor es " + num1
	print "El menor es " + num2

elif num1 < num2:
	print "El mayor es " + num2
	print "El menor es " + num1

else:
	print "Son iguales"


