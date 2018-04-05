#1)Pedir 5 datos por teclado,guardarlos en una tupla e imprimirla.

lista = []

for val in range(0,5):
	a = input("Ingrese un valor: ")
	lista.append(a)	

tupla = lista[0],lista[1],lista[2],lista[3],lista[4]

print tupla