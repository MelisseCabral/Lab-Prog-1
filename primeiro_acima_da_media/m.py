# coding: utf-8
# Melisse Cabral, 114110471
# Primeiro Acima da média

entrada = float(raw_input())
soma = 0
soma += entrada
cont = 0
cont += 1
valores = []
valores.append(entrada)

while entrada != "fim":
	entrada = raw_input()
	if entrada != "fim":
		entrada = float(entrada)
		soma += entrada
		cont += 1
		valores.append(entrada)

media  = soma / cont

for  i in range(len(valores)):
		if float(valores[i]) > media:
			print "%d, %.2f > %.2f" % (i, valores[i], media)
			break
