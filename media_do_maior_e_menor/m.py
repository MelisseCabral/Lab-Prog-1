# coding: utf-8
# Melisse Cabral, 114110471
# Média do Maior e Menor

num = int(raw_input())
maior = num
menor = num
numeros = []
cont = 0

while num >= 0:
	num = int(raw_input())
	numeros.append(num)
	if num > maior and num >= 0:
		maior = num
	if num < menor and num >= 0:
		menor = num
		
media = (maior + menor) / 2.0

print "maior: %d" % maior
print "menor: %d" % menor
print "média: %d" % media

for i in numeros:
	if i < media and i >= 0:
		 cont += 1
print "%d número(s) abaixo da média" % cont
