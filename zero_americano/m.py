# coding: utf-8
# Melisse Cabral, 114110471
# Zero Americano

def zero_ou_um(nums):
	nums = nums.split()
	soma = 0
	cont = 0
	cont2 = 0
    
    for i in nums:
		soma += int(i)
		cont += 1
        
	for i in range(soma):
		cont2 += 1
		if cont2 == (cont + 1):
		cont2 = 1
	return cont2
 
while True:
	numeros = raw_input()
	if numeros == "0" :
		break
	print zero_ou_um(numeros)
