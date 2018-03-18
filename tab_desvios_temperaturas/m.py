# coding: utf-8
# Melisse Cabral, 114110471
# Tabela Desvios Temperatura

n = int(raw_input())
soma = 0
temps =[]

for i in range(n):
	temp = float(raw_input())
	soma += temp
	temps.append(temp)
	
media = soma / n
	
for i in temps:
	dif = i - media
	if dif < 0:
		print "%.2f %.2f" % (i, dif)
	else:
		print "%.2f  %.2f" % (i, dif)
