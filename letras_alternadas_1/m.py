# coding: utf-8
# Melisse Cabral, 114110471
# Letras alternadas 1

n = int(raw_input())

def letras_alternadas(palavra):
	palavra = palavra.split()
	for i in range(len(palavra)):
		if i % 2 == 1:
			del palavra(i)
	palavra = "".join(palavra)
	return palavra
	
assert letras_alternadas("casa") == "cs"
assert letras_alternadas("exemplo") == "eepo"
assert letras_alternadas("boliche") == "blce"
assert letras_alternadas("tv") == "t"

for i in range(n):
	palavra = raw_input()
	letras_alternadas(palavra)
	print palavra
