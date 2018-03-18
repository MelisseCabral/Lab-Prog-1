# coding: utf-8
# Melisse Cabral, 114110471
# Soma Indice

numero = int(raw_input())
lista = raw_input().split()

cont = 0

for i in range(lista):
	if lista[i] + i == numero:
		cont += 1
	else:
	    print "-1"
