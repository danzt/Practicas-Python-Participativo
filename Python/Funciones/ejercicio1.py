# -*- coding: utf-8 -*-
"""1)Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas 
invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True."""

def es_palindromo(word):
	result = False

	if word == word[::-1]:
		result = True

	return result

w = input("Ingrese una palabra para reconocer si es palindromo: ")

print es_palindromo(w)