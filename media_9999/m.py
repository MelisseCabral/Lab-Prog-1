# coding: utf-8
# Melisse Cabral, 114110471
# Média 9999

num = float(raw_input())
soma = 0
cont = 0

while num != 9999:
	soma += num
	cont += 1
	num = float(raw_input())
	
media = soma / cont

print "%.1f" % media
