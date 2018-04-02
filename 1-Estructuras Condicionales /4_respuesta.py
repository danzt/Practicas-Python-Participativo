"""4)  Escriba un programa que pida dos numeros enteros y que escriba si el mayor es multiplo del menor"""

#Insercion de datos por linea de comandos
#Compilar: python 2_respuesta.py 64 4

"""Insertar argumentos por consola"""
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
num1 = arguments [0]
num2 = arguments [1]

"Conversion de srt a int "
num_1= int(num1)
num_2 =int (num2)

"""Multiplo del menor"""

if num_1 > num_2:
	multiplo = num_1 % num_2 
	if (multiplo == 0):
		print num_1, " es multiplo de ", num_2
	else:
		print num_1, " no es multiplo de ", num_2

if num_1 < num_2:
	multiplo = num_2 % num_1
	if (multiplo == 0):
		print num_2, " es multiplo de ", num_1
	else:
		print num_2, " no es multiplo de ", num_1

