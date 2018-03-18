# coding: utf-8
# Melisse Cabral, 114110471
# Soma Dos Divisiveis por 5

n = int(raw_input())
soma = 0

for i in range(1,n+1):
	num = int(raw_input())
	if num % 5 == 0:
		soma += num
print soma
