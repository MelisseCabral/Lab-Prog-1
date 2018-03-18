# coding: utf-8
# Melisse Cabral, 114110471
# Digitos coincidentes

ent1 = raw_input().split()
ent2 = raw_input().split()
soma = 0
nums = []
posicoes = []

for i in range(len(ent1)):
    if ent1[i] == ent2[i]:
        if ent1[i] in '2468':
            nums.append(ent1[i])
            posicoes.append[i]
            soma += int(ent1[i])
print "Dígitos coincidentes"
for i in range(len(nums)):
    print "%s posição %s" % (nums[i], posicoes[i])
print "Soma de digitos coinciendentes: %d" % soma                
        
