# -*- coding: utf-8 -*-
"""3)Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""

def generar_n_caracteres(number, word):
	
	new_word = word

	for x in xrange(1,number):
		new_word = new_word + word

	return new_word

word = input("Ingrese una palabra: ")
number = input("Ingrese cantidad de veces a repetir: ")

print generar_n_caracteres(number,word)