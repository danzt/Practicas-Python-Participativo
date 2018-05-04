"""2)crear una clase llamada persona, que va a tener como atributos "nombre" y "edad", con dos metodos, uno para obtener el nombre (que lo imprima por pantalla) y otro para obtener la edad, y despues una clase llamada alumno, que aparte de tener una edad y un nombre como la clase persona, tambien va a tener el atributo "nota" con un metodo para obtener la nota... usar herencia..."""

class Persona:

	def __init__(self):
		self.nombre = None
		self.edad = None
		print 'Se creo la persona'

		
	def obtener_nombre(self):
		print 'Nombre es: ', self.nombre

	def obtener_edad(self):
		print 'Edad es: ', self.edad

class Alumno(Persona):
	def __init__(self, nota):
		self.nota = nota
		print 'Nota es: ', self.nota


P = Persona()
P.nombre = "Luis"
P.edad = 12
P.obtener_nombre()
P.obtener_edad()
A = Alumno(20)
