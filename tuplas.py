primeira_tupla = ()
primeira_tupla = (1, 2, 3, 4, "Olá, tupla")
print(primeira_tupla)

# Verificar o índice do elemento 4 na tupla
try:
    indice_4 = primeira_tupla.index(4)
    print(f"O índice do elemento 4 na tupla é: {indice_4}")
except ValueError:
    print("O elemento 4 não está presente na tupla.")

# Verificar se a tupla contém o elemento 3
if 3 in primeira_tupla:
    print("A tupla contém o elemento 3.")
else:
    print("A tupla não contém o elemento 3.")

# Verificar se a tupla contém o elemento 33
if 33 in primeira_tupla:
    print("A tupla contém o elemento 33.")
else:
    print("A tupla não contém o elemento 33.")