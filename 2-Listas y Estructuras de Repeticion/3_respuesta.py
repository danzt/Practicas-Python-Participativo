"""3) Dado la siguiente lista [9,5,1,7,6,3,4,7,2,22,11,85,69,42,45,65] ordenar de menor a mayor y de mayor a menor"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

lista = [9,5,1,7,6,3,4,7,2,22,11,85,69,42,45,65]
l1 = []
l2 = []
l1 = sorted(lista)  
l2 = sorted(lista, reverse=True)

print "Lista de menor a mayor: \n", l1
print "Lista de mayor a menor: \n", l2


