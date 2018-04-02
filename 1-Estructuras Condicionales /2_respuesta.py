"""2) Escriba un programa que pida dos numeros enteros y que calcule su division, escribiendo si la division es exacta o no"""

# coding: utf-8
#!/usr/bin/python

#Insercion de datos por linea de comandos
#Compilar: python 2_respuesta.py 4 6

"""Insertar argumentos por consola"""
import sys
name = sys.argv[0]
arguments = sys.argv[1:]
num1 = arguments [0]
num2 = arguments [1]

"Conversion de srt a int "
num_1= int(num1)
num_2 =int (num2)

"Division del programa "
print "Division: " , num_1 , "/" , num_2 , "= " , num_1/num_2
print "Residuo: " , num_1 , "%" , num_2 , "= " , num_1%num_2

if (num_1 % num_2 == 0):
	print "La division es exacta"
else:
	print "La division es inexacta"


#Otra forma de imprimir 
#print "Numero 1{}".format(num_1) 
