# coding: utf-8
# Melisse Cabral, 114110471
# Combina palavras

palavra1 = raw_input()
palavra2 = raw_input()
l = ["C"]

if len(palavra1) > len(palavra2):
	palavraMaior = palavra1
	palavraMenor = palavra2
else:
	palavraMaior = palavra2
	palavraMenor = palavra1

for i in range(len(palavraMaior)):
	if i < len(palavraMenor):
		if palavraMaior[i] != palavraMenor[i]:
			l.append(palavraMenor[i])
			l.append(palavraMaior[i])
	else:
		l.append(palavraMaior[i])	 
nova_palavra = "".join(l)

print nova_palavra
		
