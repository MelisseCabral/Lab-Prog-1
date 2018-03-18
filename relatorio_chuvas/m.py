# coding: utf-8
# Melisse Cabral, 114110471
# Relatorio de chuvas

indices = raw_input().split()
meses = raw_input().split()
soma = 0
maior = 0
menor = 10000
pos_maior = 0
pos_menor = 0

for i in range(len(meses)):
	soma += float(indices[i])
	if float(indices[i]) > maior:
		maior = float(indices[i])
		pos_maior = i
	elif float(indices[i]) < menor:
		menor = float(indices[i])
		pos_menor = i
media  = soma / len(meses)
print "Mínimo: %.2f (em %s)" % (menor, meses[pos_menor])
print "Máximo: %.2f (em %s)" % (maior, meses[pos_maior])
print "Média: %.2f" % media
print "--- Abaixo da média"
for i in range(len(indices)):
	if float(indices[i]) < media:
		print "%s: %.2f" % (meses[i], float(indices[i]))
