# -*- coding: utf-8 -*-
#2) dada la siguiente lista [1,5,6,9,8,2,4,3,4,3] imprimir una nueva, 
#con la suma de cada uno de los elementos de la lista con el siguiente, 
#manteniendo el primero digito ejemplo [1,6,12,21,29...]

lista = [1,5,6,9,8,2,4,3,4,3]
l1 = []
suma = 0

for val in lista:
	suma = suma + val
	l1.append(suma)

print "Lista Original: {}".format(lista)
print "Lista Nueva: {}".format(l1)