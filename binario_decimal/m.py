# coding: utf-8
# Melisse Cabral, 1º Periodo, UFCG, 114110471
# Binario decimal

binario =  raw_input()

exp = []

for i in range(len(binario)):
   exp.append(2 ** i)

expoen = exp[::-1]
conta = []
soma = 0

for i in range(len(expoen)):
   conta.append(int(binario[i]) * int(expoen[i]))
   soma += int(conta[i])
   
   print "%d * %d = %d" % (int(binario[i]), int(expoen[i]), int(conta[i]))
print "%s(2) = %d(10)" % (binario, soma)
