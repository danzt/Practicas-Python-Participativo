# -*- coding: utf-8 -*-
#1) dada la siguiente lista [1,11,8,6,4,3,7,2,14,9] imprimir en pantalla dos nuevas listas, 
#una con los numeros pares y otra con los numeros impares

lista = [1,11,8,6,4,3,7,2,14,9]
l1 = []
l2 = []

for val in lista:
	if val%2 == 0:
		l1.append(val)
	else :
		l2.append(val)

print "Lista Original: {}".format(lista)
print "Numero Pares: {}".format(l1)
print "Numeros Inpares: {}".format(l2)