# coding: utf-8 
# Melisse Cabral, 114110471
# Eh Palindromo

palavra = raw_input()
palavra1 = "".join(palavra)
tamanho = len(palavra1)
indice = tamanho/2 + tamanho%2
cont = 0
nova_palavra = []

for i in range(indice):
   if palavra1(i) == palavra1((tamanho/2) + 1):
       nova_palavra.append(palavra(i))
   else: 
       break       
if palavra1 == "".join(nova_palavra):
    print "%s é panlindromo" % palavra
else:
       print "%s nao é panlindromo" % palavra               
   
            

