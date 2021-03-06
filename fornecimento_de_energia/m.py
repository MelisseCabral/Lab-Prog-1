# coding: utf-8
# Melisse Cabral, 114110471
# Fornecimento de energia

n = int(raw_input())

consumidores = []
categoria = []
consumos = []
gastos = []
soma_r = 0.0
soma_e = 0.0
soma_c = 0.0
cons_r = 0.0
cons_e = 0.0
cons_c = 0.0
cont = 0

for i in range(n):
	codigo = raw_input()
	consumidores.append(codigo)
	consumo = float(raw_input())
	consumos.append(consumo)
	tipo = raw_input()
	categoria.append(tipo)

for i in range(n):
	if categoria[i] == "R":
		gasto = float(consumos[i]) * 0.7
		soma_r += float(consumos[i])
		cons_r += 1
	elif categoria[i] == "E":
		gasto = float(consumos[i]) * 0.5
		soma_e += float(consumos[i])
		cons_e += 1
	else:
		gasto = float(consumos[i]) * 0.3
		soma_c += float(consumos[i])
		cons_c += 1
	gastos.append(gasto)	

media_geral = (soma_c + soma_e + soma_r) / len(consumidores)
media_r = soma_r / cons_r
media_e = soma_e / cons_e
media_c = soma_c / cons_c

print "Total do consumo (Consumidor Regular) : %.2f kWh" % soma_r
print "Total do consumo (Consumidor Especial): %.2f kWh" % soma_e
print "Total do consumo (Consumidor Carente) : %.2f kWh" % soma_c
print "---"
print "Média de consumo (Consumidor Regular) : %.2f kWh" % media_r
print "Média de consumo (Consumidor Especial): %.2f kWh" % media_e
print "Média de consumo (Consumidor Carente) : %.2f kWh" % media_c
print "---"
print "Média geral de consumo: %.2f kWh" % media_geral
print "---"
print "Consumidores acima da média geral:"
for i in range(len(consumidores)):
	if float(consumos[i]) > media_geral:
		cont += 1
		print "(%s) %5d R$ %.2f" % (categoria[i], int(consumidores[i]), gastos[i])

print "---"
