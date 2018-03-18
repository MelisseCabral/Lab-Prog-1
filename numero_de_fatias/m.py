# coding: utf-8
# Melisse Cabral, 114110471
# Número de Fatias

convidados = int(raw_input())
opcao1 = 32/convidados
resto = 32 % convidados
opcao2 = 32.0/convidados

print "Opção 1: %d fatias cada, %d de resto" % (opcao1, resto)
print "Opção 2: %.2f fatias cada" % opcao2
