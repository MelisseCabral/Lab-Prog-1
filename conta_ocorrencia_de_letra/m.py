# coding: utf-8
# Melisse Cabral, 114110471
# Conta ocorrencia de letra

letra = raw_input()
frase = raw_input()
"".join(frase)
frase.split()
cont = 0
posicao = []

for i in range(len(frase)):
	if frase[i] == letra:
		cont += 1
		posicao.append(i+1)
		
perc_ocorrencia = (float(cont) / len(frase)) * 100
posicao = (posicao)

print "Letra %s:" % letra
print "%d ocorrência(s) (%.2f %%)" % (cont,perc_ocorrencia)

if cont != 0:
	print "Na(s) posição(ões): (%s)" % posicao
	
	
