"""3)Definir una funcion generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") deberia devolver "xxxxx"."""

#!/usr/bin/python
# -*- coding: utf-8 -*-

def generar_n_caracteres(repetir, cadena):
	while (repetir != 0):
		print cadena,
		repetir = repetir -1

generar_n_caracteres(5, "x") 

	
