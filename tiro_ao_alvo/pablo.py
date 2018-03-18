# coding: utf-8

import math
contador_disparos = 0
soma_distancia = 0

while True:
    tiro = raw_input().split(",")
    distancia = math.sqrt((float(tiro[0]) ** 2) + (float(tiro[1]) ** 2))
    if distancia <= 200:
        contador_disparos += 1
        soma_distancia += distancia
        print "%.2f" % (distancia)

    if distancia > 200:
        break
media = soma_distancia / contador_disparos

print "--"
print "num disparos: %d" % (contador_disparos)
print "distancia media: %.2f" % (media)
