# coding: utf-8
# Melisse Cabral, 114110471
# Divisores Pares

num = int(raw_input())

for i in range(2,num):
	if i % 2 == 0 and num % i == 0:
		print i
