# coding: utf-8
# Melisse Cabral, 114110471
# Soma inteiros intervalos

a = int(raw_input())
b = int(raw_input())
soma = 0

for i in range(a,b+1):
	soma += i
	
print "Soma: %d" % soma
