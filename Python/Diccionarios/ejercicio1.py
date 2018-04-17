# -*- coding: utf-8 -*-
#1)Crea un diccionario vacío para guardar los datos de un paciente y, posteriormente, guarda en él 
#su edad (40), sexo (‘M’) y si es diabético (_True_). Una vez añadidos los datos, ¿cuáles serán las 
#claves y los valores del diccionario? ¿Cuántos datos tenemos sobre este paciente?, imprimir 
#diccionario.

dictionary = {}

dictionary['edad'] = input("Ingrese la edad del paciente (27): ")
dictionary['sexo'] = input("Ingrese el sexo del paciente ('M'/'F'): ")
d = input("Es diabetico el paciente ('S'/'N'):")
if d.upper() == 'S':
	dictionary['diabetico'] = True
else:
	dictionary['diabetico'] = False

print "El diccionario tiene las siguientes clases {}".format(dictionary.keys())
print "El diccionario tiene los siguientes valores {}".format(dictionary.values())
print "Tenemos {} datos del paciente".format(len(dictionary))
print "El diccionario es: {}".format(dictionary)