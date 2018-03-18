# coding: utf-8
# Melisse Cabral, 114110471
# Pontos CNH

infracoes = raw_input().split()
soma = 0

for i in infracoes:
	if i == "Gravíssima":
		soma += 7
	elif i == "Grave":
		soma += 5 
	elif i == "Média":
		soma += 4
	elif i == "Leve":
		soma += 3
		
if soma < 20 and soma >= 1:
	print "%d pontos. CNH válida." % soma
else:
	print "%d pontos. CNH suspensa." % soma
