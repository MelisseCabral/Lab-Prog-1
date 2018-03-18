# coding: utf-8
# Melisse Cabral, 114110471
# Gera Nova Palavra

palavra = raw_input()
novapalavra = []

for i in range(len(palavra)):
	if i % 2 == 0:
		novapalavra.append(palavra[i])
for i in range(len(palavra)):
	if i % 2 != 0:
		novapalavra.append(palavra[i])
novapalavra = "".join(novapalavra)
print novapalavra
