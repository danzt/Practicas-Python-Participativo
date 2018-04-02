"""1) Dada la siguiente lista [1,11,8,6,4,3,7,2,14,9] imprimir en pantalla dos nuevas listas, una con los numeros pares y otra con los numeros impares"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

lista=[1,11,8,6,4,3,7,2,14,9] 
lpar = []
limpar=[]

for i in lista:
	if (i%2==0):

		lpar.append(i)
	
	else:
		limpar.append(i)

print "Lista elementos par: ", lpar
print "Lista elementos impar: ", limpar

#Otra forma de insertar
#lpar.insert(len(lista), i)
