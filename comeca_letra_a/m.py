# coding: utf-8
# Melisse Cabral, 114110471
# Começa com a letra "A"

def testa_palavra(palavra):
	if palavra[0] == "A":
		return True
	else:
		return False

palavra = raw_input()
cont = 0
testa_palavra(palavra)

while True:
	if testa_palavra(palavra) == False:
		cont += 1
		palavra = raw_input()
		testa_palavra(palavra)
	else:
		print "---"
		print "%d %s" % (cont, palavra)
		break
