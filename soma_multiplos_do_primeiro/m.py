# coding: utf-8
# Melisse Cabral, 114110471
# Soma multiplos do primeiro

k = int(raw_input())
soma = 0

for i in range(10):
	num = int(raw_input())
	if num % k == 0:
		soma += num

print soma
