# coding: utf-8
# Melisse Cabral, 1º Periodo, UFCG, 114110471
# Octal decimal

numero =  raw_input()

exp = []

for i in range(len(numero)):
   exp.append(i)

expoen = exp[::-1]
conta = []
soma = 0

for i in range(len(expoen)):
   conta.append(int(numero[i]) * 8 ** int(expoen[i]))
   soma += int(conta[i])
   
   print "%d * 8^%d = %d" % (int(numero[i]), int(expoen[i]), int(conta[i]))
print "%s(8) = %d(10)" % (numero, soma)
