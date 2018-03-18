# coding: utf-8
# Melisse Cabral, 114110471
# Relatorio de Notas

num_alunos = int(raw_input())
aprovados = 0
reprovados = 0
soma_aprovados = 0
soma_reprovados = 0

for i in range(num_alunos):
	nota = float(raw_input())
	if nota >= 7:
		aprovados += 1
		soma_aprovados += nota
	else:
		reprovados += 1
		soma_reprovados += nota
perc_aprovados = (aprovados/float(num_alunos)) * 100.0
perc_reprovados	= (reprovados/float(num_alunos)) * 100.0

print "aprovados: %d (%.1f%%)" % (aprovados,perc_aprovados)
if aprovados != 0:
	print "nota média aprovados: %.2f" % (soma_aprovados/float(aprovados))
print "reprovados: %d (%.1f%%)" % (reprovados, perc_reprovados)
if reprovados != 0:
	print "nota média reprovados: %.2f" % (soma_reprovados/float(reprovados))
