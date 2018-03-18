# coding: utf-8
# Melisse Cabral, 114110471
# Aula de medias

soma = 0
cont = 0
nums = []

while soma < 100:
	num = float(raw_input())
	soma += num
	nums.append(num)
	cont +=1
	
media = soma / cont

print "Quantidade de números lidos: %d" % cont
print "Soma dos números lidos: %.2f" % soma
print "Média = %.2f" % media
print	
print "Abaixo da média"
for i in range(len(nums)):
	if float(nums[i]) < media:
		print "%.2f (%do)" % (nums[i], i+1)
print
print "Acima da média"
for i in range(len(nums)):
	if float(nums[i]) > media:
		print "%.2f (%do)" % (nums[i], i+1)
