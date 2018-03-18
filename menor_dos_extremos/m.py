# coding: utf-8
# Melisse Cabral, 114110471
# Menor dos Extremos

n = int(raw_input())
lista = []
menor = 0
cont_menor = 0
cont_maior = 0

for i in range(n):
	num = int(raw_input())
	lista.append(num)
	
if int(lista[0]) >= int(lista[-1]):
	menor  = int(lista[-1])
else:
	menor = int(lista[0])
	
for i in lista:
	if i < menor:
		cont_menor += 1
	elif i > menor:
		cont_maior += 1
print "Menor dos extremos: %d" % menor
print "%d número(s) abaixo do menor" % cont_menor
print "%d número(s) acima do menor" % cont_maior

		
		
	
