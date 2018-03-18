# coding: utf-8
# Melisse Cabral, 114110471
# Tabela Quadrados Divisiveis por 3

x = int(raw_input())
y = int(raw_input())

if y >= x:
	for i in range(x,y+1):
		if i ** 2 % 3 == 0:
			print "%d %d *" % (i, i**2)
		else:
			print i, i**2
else:
	print "---"
