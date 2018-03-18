# coding: utf-8
# Melisse Cabral, 114110471
# Exercicios Resolvidos

exercicios = raw_input().split()
alunos = raw_input().split()
maior = 0
pos = 0

for i in range(len(alunos)):
	if int(exercicios[i]) > maior:
		maior = int(exercicios[i])
		pos = i

print "%s %d" % (alunos[pos], maior)
