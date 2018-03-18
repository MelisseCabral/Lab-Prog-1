# coding: utf-8
# Melisse Cabral, 114110471
# Quantidade de números impares

pares = 0
impares = 0
soma_pares = 0
soma_impares = 0

def quant_par_impar(num):
	if num % 2 == 0:
		pares += 1
		soma_pares += num
	else:
		impares += 1
		soma_impares += num
	return

num = int(raw_input())
if num != 0:
	quant_par_impar(num)

while num != 0:
	num = int(raw_input())
	quant_par_impar(num)

media = (soma_impares + soma_pares) / (pares/impares)

print "pares: %d" % pares
print "impares: %d" % impares
print "media pares: %.1f" % (float(soma_pares) / pares)
print "media impares: %.1f" % (float(soma_impares) / impares)
print "media geral: %.1f" % media
	
