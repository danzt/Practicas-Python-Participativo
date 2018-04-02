# 4) introducir un ano por teclado y decir a que siglo pertenece ese ano

"""
-separo todo
meto dos elemtos en una lista 
- meto los otros dos en otra"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
l2=[]
ly=[]
year=int(input("Ingrese ano para conocer su siglo: "))

if (year>=1000):
 	while year>0:
		b=year%100	
		year=year/100
		l2.append(b)

	l3=l2[::-1]
	
	if (l3[1] == 00):
		print "Siglo:", l3[0]
	else: 
		print "Siglo:", l3[0]+1

else:
		year=str(year).zfill(4)
		ly=map(int, year)
		print "Siglo:", ly[0]+ly[1]+1






