# coding: utf-8
# Melisse Cabral, 114110471
# Média Palavras

palavra = raw_input()
soma = 0
cont = 0

while palavra != "fim":
	soma += len(palavra)
	cont += 1
	palavra = raw_input()
	
if cont != 0:
	media = soma/float(cont)
	print "%.1f" % media
else:
	print "0.0"
