"""1)Definir una funcion es_palindromo() que reconoce palindromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendria que devolver True."""

#!/usr/bin/python
# -*- coding: utf-8 -*-

def es_palindromo(palabra):

	if palabra == palabra[::-1]: 
		print  palabra, 'es', True
	else:
		print palabra, 'es', False
 
es_palindromo('radar')
es_palindromo('radio')



