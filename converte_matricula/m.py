# coding: utf-8
# Melisse Cabral, 114110471
# Converte Matricula

matricula = raw_input()
nova_matricula = []

for i in range(len(matricula)):
    if i == 5:
	nova_matricula.append(matricula[i])
	nova_matricula.append("0")
    elif i == 0:
	nova_matricula.append("1")
    else:
	nova_matricula.append(matricula[i])

nova_matricula = "".join(nova_matricula)
print nova_matricula
