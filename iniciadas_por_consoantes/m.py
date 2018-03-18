# coding: utf-8
# Melisse Cabral, 114110471
# Iniciada Por Consoante

n = int(raw_input())
cont =0

for i in range(n):
	palavra = raw_input()
	if palavra[0] not in "AaEeIiOoUu":
		cont +=1

perc = (cont/(float(n))) * 100

print "total de palavras: %d" % n
print "iniciadas por consoantes: %d (%.2f%%)" % (cont, perc) 
