"""4)Introducir por teclado 3 palabras y devolver un diccionario donde la key sea la palabra ingresada, y el valor sea la cantidad de caracteres que posee dicha palabra, ejemplo {'abogado':7}"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

keys=[]
values=[]
n=1

while (n <= 3):
	palabra=raw_input("Introduce la palabra: ")
	keys.append(palabra)
	n=n+1	

long1=len(keys[0])
long2=len(keys[1])
long3=len(keys[2])
values =[long1, long2, long3]

dic = dict(zip(keys,values))

print dic








