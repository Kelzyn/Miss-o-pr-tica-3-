lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Conteúdo inicial da lista
print("Conteúdo da lista antes de adicionar o elemento:")
print(lista_mesclada)

# Utilizando o método "append" para adicionar um elemento à lista
lista_mesclada.append(["Lista aninhada"])

# Conteúdo da lista após adicionar o elemento
print("Conteúdo da lista após adicionar o elemento:")
print(lista_mesclada)

# Conteúdo da lista antes da inserção
print("Conteúdo da lista antes de inserir o elemento:")
print(lista_mesclada)

# Utilizando o método "insert" para inserir o elemento na posição 4
elemento_inserido = 5
lista_mesclada.insert(4, elemento_inserido)

# Imprimir o conteúdo da lista após a inserção
print("Conteúdo da lista após inserir o elemento 5 na posição 4:")
print(lista_mesclada)

# Imprimir o conteúdo atual da lista
print("Conteúdo atual da lista:")
print(lista_mesclada)

# Imprimir o tamanho atual da lista
print("Tamanho atual da lista:")
print(len(lista_mesclada))

# Remover o item na posição 1 da lista
del lista_mesclada[1]

# Imprimir o conteúdo atualizado da lista
print("Conteúdo atualizado da lista após remover o item na posição 1:")
print(lista_mesclada)

# Criar uma nova lista chamada "nova_lista_mesclada" e adicionar os itens até a posição 4 da lista anterior
nova_lista_mesclada = lista_mesclada[:4]

# Imprimir o conteúdo da nova lista
print("Conteúdo da nova lista 'nova_lista_mesclada':")
print(nova_lista_mesclada)

# Imprimir o conteúdo da nova lista
print("Conteúdo da nova lista 'nova_lista_mesclada':")
print(nova_lista_mesclada)