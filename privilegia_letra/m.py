# coding: utf-8
# Melisse Cabral, 114110471
# Privilegia Letra

def letra_magica(fila, letra):
    cont_troca = 0
    for i in range(len(fila)):
        if (fila[i][0]).upper() == letra.upper():
            chave = fila[cont_troca]
            fila[cont_troca] = fila[i]
            fila[i] = chave
            cont_troca += 1
    return fila
letra = 'a'         
fila = ["Jorge", "Dalton", "alberto", "Adriana", "Eliane", "Toni", "Chico", "Marcelo", "Marcos", "Antonio", "Amarildo", "Carla", "Maria"]
print letra_magica(fila, "a")
#assert fila == ["Alberto", "Adriana", "Antonio", "Amarildo", "Eliane", "Toni", "Chico", "Marcelo", "Marcos","Jorge", "Dalton",  "Carla", "Maria"]
