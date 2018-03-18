# coding: utf-8
# Melisse Cabral, 114110471
# Classifica Cada Letra

palavra = raw_input()

for i in range(len(palavra)):
	if palavra[i] in "AaEeIiOoUu":
		print "<%s> sim" % palavra[i]
	elif palavra[i] in "1234567890":
		print "<%s> nao" % palavra[i]
	else:
		print "<%s> nao" % palavra[i]
