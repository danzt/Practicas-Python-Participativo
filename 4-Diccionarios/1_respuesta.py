"""1)Crea un diccionario vacio para guardar los datos de un paciente y, posteriormente, guarda en el su edad (40), sexo (M) y si es diabetico (_True_). Una vez anadidos los datos, Cuales seran las claves y los valores del diccionario. Cuantos datos tenemos sobre este paciente, imprimir diccionario. """

#!/usr/bin/python
# -*- coding: utf-8 -*-

datos_paciente = {}

edad = int(input("Inserte la edad del paciente: "))
sexo = raw_input("Inserte el sexo del paciente(F/M): ")
diabetico = raw_input("Inserte la condicion de diabetico (si/no): ")

datos_paciente['edad'] = edad
datos_paciente['sexo'] = sexo

if (diabetico =="si"):
	datos_paciente['diabetico'] = "_True_"
else: 
	datos_paciente['diabetico'] = "_False_"

print "\nDatos paciente =", datos_paciente

keys = datos_paciente.keys()
values = datos_paciente.values()

print "\nClaves = ", keys
print "Datos = ", values
