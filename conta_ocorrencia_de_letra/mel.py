# coding: utf-8
# Melisse Cabral, 114110471
# Conta Ocorrencia de letra

letra = raw_input()
palavra = raw_input()
pos = []
cont = 0

for i in range(len(palavra)):
    if palavra[i] == letra:
        cont += 1
        pos.append(i+1)

perc = (cont / len(palavra))  * 100.0

print "Letra %s:" % letra
print "%d ocorrência(s) (%.2f %%)" % (cont, perc)
if cont != 0:
    print "Na(s) posição(ões): (%s)" % pos[1:-1]
