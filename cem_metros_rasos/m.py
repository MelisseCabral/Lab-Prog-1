# coding: utf-8
# Melisse Cabral, 114110471
# Cem Metros Rasos

n = int(raw_input())
cont = 0
competidores = []
medias = []
menorestempos = []
menor_tempo = 0
menor_tempo_medio = 0
competidor_menor_tempo = ""
competidor_menor_media = ""

while cont <= n:
	competidor = raw_input().split(",")
	competidores.append(competidor[0:1])
	soma = 0
	for i in range(2,len(competidor)):
		soma += float(competidor[i])
	media = soma / (len(competidor)-1)
	medias.append(media)
	if cont == 0:
		menor_tempo_medio = media
		competidor_menor_tempo = competidor[0:1]
	elif media < menor_tempo_medio:
		menor_tempo_medio = media
		competidor_menor_tempo = competidor[0:1]
for  i in range(competidores):
	print "%s: média = %.2f, menor = %.2f" % (competidores[i], medias[i], menor_tempo[i]) 

print "Menor tempo: %s, %.2f" % (competidor_menor_tempo, menor_tempo_medio)
print "Menor média: %s, %.2f" % (competidor_menor_media, menor_tempo)
