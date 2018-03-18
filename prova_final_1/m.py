# coding: utf-8
# Melisse Cabral, 114110471
# Prova Final 1

alunos = int(raw_input())
final = 0
notas = 0
perc_final = 0

for i in range(alunos):
	nota = float(raw_input())
	if nota < 7:
		final +=1
		notas += nota
		media = notas/final
		perc_final = ((final/float(alunos)) * 100)

print "%d (%.1f%%) alunos na final" % (final,perc_final)
if final > 0:
	print "Média das notas: %.1f" %  media
