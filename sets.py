set_inicial = set()
set_inicial = {11, 12, 13, 14}
print(set_inicial)

# Criando o set_inicial e adicionando o elemento 15
set_inicial = set()
set_inicial.add(15)
print("Conteúdo do set após adicionar o elemento 15:", set_inicial)

# Atualizando o set_inicial com os elementos 1, 2, 3, 4, 5
set_inicial.update([1, 2, 3, 4, 5])
print("Conteúdo do set após atualização:", set_inicial)

# Removendo o elemento 13 do set_inicial (se existir)
set_inicial.discard(13)
print("Conteúdo do set após remover o elemento 13:", set_inicial)

# Criando o novo_set com os elementos 20, 21, 23, 1, 2
novo_set = set([20, 21, 23, 1, 2])
print("Conteúdo do novo set:", novo_set)

# União entre set_inicial e novo_set
uniao = set_inicial.union(novo_set)
print("Resultado da união entre os dois sets:", uniao)

# Interseção entre set_inicial e novo_set
intersecao = set_inicial.intersection(novo_set)
print("Resultado da interseção entre os dois sets:", intersecao)

# Diferença entre set_inicial e novo_set
diferenca = set_inicial.difference(novo_set)
print("Resultado da diferença entre os dois sets (set_inicial - novo_set):", diferenca)

# Diferença simétrica entre set_inicial e novo_set
dif_simetrica = set_inicial.symmetric_difference(novo_set)
print("Resultado da diferença simétrica entre os dois sets:", dif_simetrica)