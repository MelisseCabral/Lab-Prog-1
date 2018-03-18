# coding: utf-8
# Melisse Cabral, 114110471
# Pegador 

n = int(raw_input())
maior_pegada = 0
horarios = []
pegadas = []

for i in range(n):
     hora_pegada = raw_input().split()
     tempo =  int(hora_pegada[1]) - int(hora_pegada[0])
     if tempo >= maior_pegada:
         maior_pegada = tempo
     horarios.append(int(hora_pegada[0]))
     horarios.append(int(hora_pegada[1]))
     pegadas.append(tempo)

p_sem_pegar = horarios[-1] - horarios[0]
conversando = p_sem_pegar

for i in pegadas:
   conversando -= i

print "%d horas durou a maior pegada" % maior_pegada
print "%d horas sem pegar ninguem" % conversando

