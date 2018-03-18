# coding: utf-8
# Melisse Cabral, 114110471
# Conta Coincidencias

def conta_coincidencias(lista1, lista2):
	cont = 0
	if len(lista1) > len(lista2):
		maior = lista1
		menor = lista2
	else:
		maior = lista2
		menor = lista1
	for i in range(len(menor)):
		if menor[i] == maior[i]:
			cont += 1
	return cont
lista1 = raw_input().split()
lista2 = raw_input().split()

x = conta_coincidencias(lista1, lista2)

print x
