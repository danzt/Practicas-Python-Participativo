# -*- coding: utf-8 -*-
"""4)introducir por teclado 3 palabras y devolver un diccionario donde la key sea la palabra 
ingresada, y el valor sea la cantidad de caracteres que posee dicha palabra, ejemplo {'abogado':7}"""

a = input("Ingrese una palabra: ")
b = input("Ingrese una palabra: ")
c = input("Ingrese una palabra: ")

dic = {}

dic[a] = len(a)
dic[b] = len(b)
dic[c] = len(c)

print "El diccionario generado es: {}".format(dic)

