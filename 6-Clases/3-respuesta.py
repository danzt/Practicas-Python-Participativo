"""3)Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el metodo __init__. Calcular despues la suma, resta, multiplicacion y division. Utilizar un metodo para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora."""


class Calculadora:

	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		print 'Se creo la calculadora'

		
	def suma(self):
		print 'Suma es: ', self.num1+self.num2

	def resta(self):
		print 'Resta es: ', self.num1-self.num2

	def multiplicacion(self):
		print 'Multiplicacion es: ', self.num1*self.num2

	def division(self):
		print 'Division es: ', self.num1/self.num2



a=int(input("Inserte un numero: "))
b=int(input("Inserte otro numero: "))

c=Calculadora(a, b)
c.suma()
c.resta()
c.multiplicacion()
c.division()







