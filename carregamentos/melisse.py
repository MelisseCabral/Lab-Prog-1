# coding: utf-8
# Melisse Cabral, 114110471
# Carregamento

n = int(raw_input())
tempo_max = 0.0
cont = 1
posicao = 1

while cont <= n:
	horario = raw_input().split()
	tempo = int(horario[1]) - int(horario[0])
	if tempo >= tempo_max:
		tempo_max = tempo
		posicao = cont
	cont += 1
		
print "carregamento %d" % posicao
