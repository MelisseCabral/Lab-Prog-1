# coding: utf-8
# Melisse Cabral, 114110471
# Numeros Oscilantes

num = raw_input()

def testa_num1(num):
	for i in range(0,len(num),2):
		if int(num[i]) % 2 == 0 and int(num[i + 1]) % 2 != 0:
			return True
		else: 
			False
			
def testa_num2(num):
	for i in range(0,len(num),2):
		if int(num[i]) % 2 != 0 and int(num[i + 1]) % 2 == 0:
			return True
		else: 
			False
if testa_num1(num) == True or testa_num2(num) == True and testa_num1(num) != testa_num2(num):
	print "Verdadeiro: %d algorismos." % len(num)
else: 
	print "Falso: %d algorismos." % len(num)
