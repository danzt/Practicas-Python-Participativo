"""3) Escriba un programa que pida el ano actual y un ano cualquiera  y que escriba cuantos anos han pasado desde ese ano o cuantos anos faltan para llegar a ese ano"""

# coding: utf-8
#!/usr/bin/python

#Insercion de datos por linea de comandos
#python 3_respuesta.py 2018 2019

"""Insertar argumentos por consola"""
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
year1 = arguments [0]
year2 = arguments [1]

"Conversion de srt a int "
year_1= int(year1)
year_2 =int (year2)

"""Anos que faltan"""
year_3 = abs(year_1 - year_2)

if (year_1 > year_2):
	print "Faltan: ", year_3, "anos desde: " , year_1, "a ", year_2

else: 

	print "Han Pasado: ", year_3, "anos desde: " , year_1, "a ", year_2



