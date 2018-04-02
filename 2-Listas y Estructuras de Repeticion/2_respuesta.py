"""2) dada la siguiente lista [1,5,6,9,8,2,4,3,4,3] imprimir una nueva, con la suma de cada uno de los elementos de la lista con el siguiente, manteniendo el primero digito ejemplo [1,6,12,21,29...]"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

lista = [1,5,6,9,8,2,4,3,4,3]
lnueva=[]

suma = 0
for i in lista:
	
	suma += i
	lnueva.append(suma)

print lnueva
