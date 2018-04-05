# -*- coding: utf-8 -*-
#2)Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores 
#de la tupla en cuyo indice.

tupla = (10,1,9,2,8,3,7,4,5,6)

i = input("Ingrese un valor del 1 al 10 para ver su valor en la tupla: ")

print "El valor de la tupla es : {}".format(tupla[i-1])

