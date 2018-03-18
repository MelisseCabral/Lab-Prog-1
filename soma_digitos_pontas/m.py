# coding: utf-8
# Melisse Cabral, 114110471
# soma digitos pontas

# Recebe String de inteiro com len = 5
num = raw_input()
# Transforma os dois primeiros elementos em um inteiro e soma aos dois ultimos elementos
soma = int(num[0:2]) + int(num[3:5])
# Multiplica a soma pelo elemento do meio
num_final = soma * int(num[2])
# Define função para a formatação de saida
if num_final < 100:
	print "00%d" % num_final
elif num_final >= 100 and num_final < 1000:
	print "0%d" % num_final
elif num_final >= 1000:
	print "%d" % num_final
else:
	print "000%d" % num_final
