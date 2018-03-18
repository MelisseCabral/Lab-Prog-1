# coding: utf-8
# Melisse Cabral, 114110471
# Começo palavra

n = int(raw_input())
letra = raw_input()
cont = 0

while cont == n:
	palavra = raw_input()
	if palavra[0] == letra:
		print "n? c? palavra? %s comeca com p" % palavra
	else:
		print "palavra? %s nao comeca com p" % palavra
