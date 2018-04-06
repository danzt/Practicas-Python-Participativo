# -*- coding: utf-8 -*-
#2)introducir por teclado una cadena y devuelva un diccionario con la cantidad de apariciones de 
#cada palabra en la cadena. Por ejemplo, si recibe  _"que lindo día que hace hoy"_  debe devolver: 
# `'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1`.

a = str(input("introdusca una cadena de texto: "))

dic = dict.fromkeys(a.split(' '),0)

for val in a.split(' '):
	if val in a:
		dic[val] = dic[val] + 1

print dic