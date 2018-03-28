# -*- coding: utf-8 -*-
#3) dado la siguiente lista [9,5,1,7,6,3,4,7,2,22,11,85,69,42,45,65] ordenar de menor a mayor y de mayor a menor

lista = [9,5,1,7,6,3,4,7,2,22,11,85,69,42,45,65]

l1 = lista
l2 = lista

print "Lista Original: {}".format(lista)
print "Lista menor a mayor: {}".format(sorted(l1))
print "Lista mayor a menor: {}".format(sorted(l2,reverse=True))