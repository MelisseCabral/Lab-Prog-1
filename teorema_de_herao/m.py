# coding: utf-8
# Melisse Cabral, 114110471
# Teorema De Herão

import math

num_triangulo = int(raw_input())
cont = 0
soma = 0

for i in range(num_triangulo):
	lados = raw_input().split()
	a = float(lados[0])
	b = float(lados[1])
	c = float(lados[2])
	s = (a + b + c) / 2
	area = math.sqrt(s * (s - a) * (s - b) * (s - c))
	if area >= 100:
		cont += 1
		soma += area
	print "Área %d: %.2f" % ((i+1), area)
	
if cont > 0:
	media = soma / cont
	print "Número maiores: %d, área média: %.2f" % (cont, media)
