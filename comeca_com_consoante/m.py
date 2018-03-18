# coding: utf-8
# Melisse Cabral, 114110471
# Começa com consoante

soma_palavra = 0
 
while True:
    palavra = raw_input()
    if palavra == "***":
        break
    elif palavra[0] not in "AaEeIiOoUu":
        soma_palavra += 1
print "Palavras: %d" % (soma_palavra)    
