# coding: utf-8
# Melisse Cabral, 114110471
# Digito Verificador

num_conta = raw_input()
soma = 0

for i in range(len(num_conta)):
	soma += int(num_conta[i])
	
dv = soma % 11

if dv == 10:
	print "%s-X" % num_conta
else:
	print "%s-%d" % (num_conta, dv)
