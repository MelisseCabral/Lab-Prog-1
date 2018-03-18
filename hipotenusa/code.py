# coding: utf-8
# Melisse Cabral, 114110471
# Hipotenusa

cateto1 = float(raw_input("Medida do Cateto 1? "))
cateto2 = float(raw_input("Medida do Cateto 2? "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)

print "Medida da Hipotenusa: %.2f" % hipotenusa
