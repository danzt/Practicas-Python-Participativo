""" 3)ingresar una fecha por teclado que cumpla con este formato(Dia, Mes, Ano) (donde Dia, Mes y Ano son numeros enteros) calcule el dia siguiente al dado, en el mismo formato e imprimir ambas tuplas 'fecha ingresada' y 'fecha del dia siguiente'!"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

dia = int(input("Inserte en digitos el dia: " ))
if dia>0 and dia<=31:
	print "Dia valido!"
else:
	dia = int(input("Dia invalido!. Inserte nuevamente el dia: " ))	


mes = int(input("\nInserte en digitos el mes: " ))
if mes>0 and mes<=12:
	print "Mes valido!"
else: 
	mes = int(input("Mes invalido!. Inserte nuevamente el mes: " ))


ano = int(input("\nInserte en digitos el ano: " ))
if ano>0:
	print "Ano valido!"
else: 
	ano = int(input("Ano invalido!. Inserte nuevamente el ano: " ))


fecha=(dia, mes, ano)
print "\nFecha ingresada = ", fecha

if (dia==31) and (mes==12):
	fecha_siguiente= (1, 1, ano+1)
	print "Fecha siguiente = ", fecha_siguiente

elif (dia==31) and (mes!=12):
	fecha_siguiente= (1, mes+1, ano)
	print "Fecha siguiente = ", fecha_siguiente

else:
	fecha_siguiente= (dia+1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

