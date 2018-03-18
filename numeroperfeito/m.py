# coding: utf-8
# Melisse Cabral, 114110471
# Numero Perfeito

num = int(raw_input())
soma = 0

for i in range(1,num):
	if num % i == 0:
		soma += i
if num == soma:
	print "%d é um número perfeito." % num
else:
	print "%d não é um número perfeito." % num
