# coding: utf-8
# Melisse Cabral, 114110471
# Receita e Mês

lucro = []

meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

for i in range(12):
    numero = raw_input().split()
    lucro.append(float(numero[0]) - float(numero[1]))

for i in range(len(meses)):
    print "%s %4.1f" % (meses[i] , lucro[i]) 

    
