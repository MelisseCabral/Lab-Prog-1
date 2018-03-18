# coding: utf-8
# Melisse Cabral, 114110471
# Mais Consoantes

def conta_letra(palavra):
	vogais = 0
	for i in palavra:
		if i in "aeiouAEIOU":
			vogais += 1
	consoantes = len(palavra) - vogais		
	if vogais < consoantes:
		return True
	else:
		return False
	consoantes = len(palavra) - vogais
	
cont = 1
palavra = raw_input()
if conta_letra(palavra) == True:
		print cont

while True:
	cont += 1
	palavra = raw_input()
	if conta_letra(palavra) == True:
		print cont
		break
