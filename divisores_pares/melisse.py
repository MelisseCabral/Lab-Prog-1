# coding: utf-8
# Melisse Cabral, 114110471
# Divisores Pares

num = int(raw_input())

for i in range(2,10,2):
	if num % i == 0:
		print i
