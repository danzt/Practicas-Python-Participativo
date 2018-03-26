# -*- coding: utf-8 -*-
#3)Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado 
#desde ese año o cuántos años faltan para llegar a ese año.

a = int(input("Ingrese el anio actual: "))

b = int(input("Ingrese un anio cualquiera: "))

if a > b:
	print "Han pasado {} anios desde el {} al anio actual".format(a-b,b)
elif a < b:
	print "Faltan {} anios para llegar al {}".format(b-a,b)
else :
	print "Esta en el mismo anio {}".format(b)