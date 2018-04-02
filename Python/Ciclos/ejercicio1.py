#pedir dos numero por teclado y validar el tipo de dato de cada variable, 
#si es string pedir nuevamente el ingreso del numero hasta que sea un entero y si es entero realizar una suma de ambos.

a = raw_input("Ingrese un valor numerico: ")

while not a.isdigit() :
	a = raw_input("Solo Valores numericos: ")

b = raw_input("Ingrese un valor numerico: ")

while not b.isdigit() :
	b = raw_input("Solo Valores numericos: ")

print "la suma de los valores es: {}".format(int(a)+int(b))