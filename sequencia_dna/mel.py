# coding: utf-8
# Melisse Cabral, 114110471
# Sequencia dna

seq1 = raw_input()
seq2 = raw_input()
cont = 0

if len(seq1) == len(seq2):
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			cont += 1
            
if cont > (len(seq1)/2):
	print "sim"  

else:
	print "nao"
