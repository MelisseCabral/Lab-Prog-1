# coding: utf-8
# Melisse Cabral, 114110471
# MRU

s0 = int(raw_input("posição inicial (m)?"))
vel = int(raw_input("velocidade (m/s)?")) 
tempo = float(raw_input("tempo (s)?"))
posicao_final = s0 + vel * tempo

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (tempo, posicao_final)
