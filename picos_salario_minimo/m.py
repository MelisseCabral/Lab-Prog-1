# coding: utf-8
# Melisse Cabral, 114110471
# Picos Salario Minimo

ano_inicial = int(raw_input())
ano_final = int(raw_input())
anos = range(ano_inicial, ano_final + 1)
salarios = []
cotacoes = []
precosdolar = []

for i in range(len(anos)):
	salarios.append(raw_input())
for i in range(len(anos)):
	cotacoes.append(raw_input())
for i in range(len(salarios)):
	precodolar = float(salarios[i]) / float(cotacoes[i])
	precosdolar.append(precodolar)
maximo = max(precosdolar)
minimo = min(precosdolar)
for i in range(len(anos)):
	if precosdolar[i] == maximo:
		print "%s: R$%.2f = U$%.2f (**)" % (anos[i], float(salarios[i]), float(precosdolar[i]))
	if precosdolar[i] == minimo:
		print "%s: R$%.2f = U$%.2f (*)" % (anos[i], float(salarios[i]), float(precosdolar[i]))
	elif precosdolar[i] != maximo and precosdolar[i] != minimo:
		print "%s: R$%.2f = U$%.2f" % (anos[i], float(salarios[i]), float(precosdolar[i]))
