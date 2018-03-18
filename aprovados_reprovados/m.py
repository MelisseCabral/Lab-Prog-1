# coding: utf-8
# Melisse Cabral, 114110471
# Aprovados Reprovados

n = int(raw_input())
soma_aprovados = 0
soma_reprovados = 0
aprovados = 0
reprovados = 0

for i in range(n):
	nota = float(raw_input())
	if nota >= 7:
		aprovados += 1 
		soma_aprovados += nota
	else: 
		reprovados += 1
		soma_reprovados += nota

print "Reprovados: %d" % reprovados
if reprovados != 0:
	media_b = soma_reprovados/reprovados
	print "Média: %.1f" % media_b
print
print "Aprovados: %d" % aprovados
if aprovados != 0:
	media_a = soma_aprovados/aprovados
	print "Média: %.1f" % media_a
