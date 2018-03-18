# coding: utf-8
# Melisse Cabral, 114110471
# Ataque Mais Positivo

n = int(raw_input())

clubes = []
placares = []
maior = 0
soma = 0

for i in range(n):
	clubes.append(raw_input())
	placares.append(int(raw_input()))
	soma += float(placares[i])
	if int(placares[i]) > maior:
		maior = float(placares[i])
		pos = i

print "Time(s) com melhor ataque (%d gol(s)):" %(maior)
print clubes[pos]

for i in range(len(clubes)):
	if pos != i and placares[i] == maior:
		print clubes[i]

media = soma / float(n)

print 
print "Média de gols marcados: %.1f" % (media)
	
