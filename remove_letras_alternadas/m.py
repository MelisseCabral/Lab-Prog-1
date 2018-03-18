# coding: utf-8
# Melisse Cabral, 114110471
# Remove Letras Alternadas

palavra = raw_input()
nova_palavra = ""

for i in range(len(palavra)):
    if i % 2 == 0:
        nova_palavra += palavra[i]

print nova_palavra
