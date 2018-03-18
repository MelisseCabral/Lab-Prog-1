# coding: utf-8
# Melisse Cabral, 114110471
# SAMU

atendimentos = []
soma = 0

for i in range(12):
	num = raw_input()
	atendimentos.append()
	soma += int(num)
media = soma/12.0

for i in range(len(atendimentos)):
	if int(atendimentos[i]) >= media:
		print "Mês %d: %s" % (i + 1, atendimentos[i])
	
	
	
