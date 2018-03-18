# coding: utf-8
# Melisse Cabral, 114110471
# Conta divisiveis

k = int(raw_input())
n = int(raw_input())
cont = 0

for i in range(n):
	num = int(raw_input())
	if num % k == 0:
		cont += 1
print "%d (%.1f%%)" % (cont, (float(cont)/n) * 100)
