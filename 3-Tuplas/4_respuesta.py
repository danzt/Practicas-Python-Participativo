"""4)ingresar una fecha por teclado que cumpla con este formato(Dia, Mes, Ano) (donde Dia y Ano son numeros enteros y Mes es un string 'enero','febrero'...) calcule el dia siguiente al dado, en el mismo formato e imprimir ambas tuplas 'fecha ingresada' y 'fecha del dia siguiente'."""

#!/usr/bin/python
# -*- coding: utf-8 -*-


dia = int(input("Inserte en digitos el dia: " ))
if dia>0 and dia<=31:
	print "Dia valido!"
else:
	dia = int(input("Dia invalido!. Inserte nuevamente el dia: " ))	


mes = raw_input("Inserte en string el mes: " )
if not mes.isdigit():
	print "Mes valido!"
else: 
	mes = int(input("Mes invalido!. Inserte nuevamente el mes: " ))


ano = int(input("\nInserte en digitos el ano: " ))
if ano>0:
	print "Ano valido!"
else: 
	ano = int(input("Ano invalido!. Inserte nuevamente el ano: " ))


fecha=(dia, mes, ano)
print "Fecha ingresada = ", fecha

mes=mes.lower()

if dia==31 and mes=="enero":
	mes = "Febrero"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==28 and mes=="febrero":
	mes = "Marzo"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==31 and mes=="marzo":
	mes = "Abril"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==30 and mes=="abril":
	mes = "Mayo"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==31 and mes=="mayo":
	mes = "Junio"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==30 and mes=="junio":
	mes = "Julio"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==31 and mes=="julio":
	mes = "Agosto"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==31 and mes=="agosto":
	mes = "Septiembre"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==30 and mes=="septiembre":
	mes = "Octubre"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==31 and mes=="octubre":
	mes = "Noviembre"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente


elif dia==30 and mes=="noviembre":
	mes = "Diciembre"
	fecha_siguiente= (1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente

elif dia==31 and mes=="diciembre":
	mes = "Enero"
	fecha_siguiente= (1, mes, ano+1)
	print "Fecha siguiente = ", fecha_siguiente

else:
	fecha_siguiente= (dia+1, mes, ano)
	print "Fecha siguiente = ", fecha_siguiente









