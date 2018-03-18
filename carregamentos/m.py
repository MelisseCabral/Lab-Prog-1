# coding: utf-8
# Melisse Cabral, 114110471
# Carregamento

n = int(raw_input())
tempo = []
tempo_max = 0
cont = 0

for i in range(n):
	horario = raw_input().split()
	tempo.append(int(horario[1]) - int(horario[0]))
	if 	tempo[i] > tempo_max:
		tempo_max = tempo[i]
		cont += 1
		
print "carregamento %d" % cont
    
