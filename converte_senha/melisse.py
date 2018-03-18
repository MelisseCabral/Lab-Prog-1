# coding: utf-8
# Melisse Cabral, 114110471
# Converte Senha

def trocaletra(nl):
	if nl == "A" or nl == "a":
		nl = "4"
	elif nl == "E" or nl == "e":
		nl = "3"
	elif nl == "I" or nl == "i":			
		nl = "1"
	else:
		nl = "0"
    
senha = raw_input()
senha.split()
cont = 0
    
for i in range(1,len(senha)):
	if senha[i] in "AaEeIiOo":
		trocaletra(senha[i])	
		cont += 1
"".join(senha)
print "%s (%d troca(s))" % (senha, cont)
