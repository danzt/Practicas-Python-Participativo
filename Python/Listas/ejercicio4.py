# -*- coding: utf-8 -*-
#4) introducir un ano por teclado y decir a que siglo pertenece ese ano

year = input("Ingrese un año: ")

yearStr = str(year)

if len(yearStr) < 4:
	if yearStr[1:3] == "00":
		print "Pertenece al siglo: {}".format(yearStr[:1])
	else:
		print "Pertenece al siglo: {}".format(int(yearStr[:1])+1)
else:
	if yearStr[2:4] == "00":
		print "Pertenece al siglo: {}".format(yearStr[:2])
	else:
		print "Pertenece al siglo: {}".format(int(yearStr[:2])+1)