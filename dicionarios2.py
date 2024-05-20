# Criando o dicionário inicial
dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

# Utilizando o método "update" para adicionar novos elementos ao dicionário
dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'portuguesa'},
    3: {'nome': 'Ana', 'idade': 25, 'nacionalidade': 'espanhola'}
})

# Imprimindo o dicionário recém-atualizado
print("Dicionário recém-atualizado:", dicionario)

# Criando uma cópia do dicionário
copia_dicionario = dicionario.copy()

# Removendo um elemento do primeiro dicionário com o método "pop"
elemento_removido = dicionario.pop(2)
print("Elemento removido com o método 'pop':", elemento_removido)

# Removendo o último elemento do primeiro dicionário com o método "popitem"
ultimo_elemento_removido = dicionario.popitem()
print("Último elemento removido com o método 'popitem':", ultimo_elemento_removido)

# Removendo todos os elementos dos dois dicionários com o método "clear"
dicionario.clear()
copia_dicionario.clear()

# Usando o método "fromKeys" para definir um novo dicionário
novo_dicionario = dict.fromkeys(['a', 'b', 'c'], 0)

# Imprimindo o conteúdo do novo dicionário
print("Conteúdo do novo dicionário:", novo_dicionario)

# Imprimindo apenas as chaves do novo dicionário com o método "keys"
print("Chaves do novo dicionário:", novo_dicionario.keys())

# Imprimindo apenas os valores do novo dicionário com o método "values"
print("Valores do novo dicionário:", novo_dicionario.values())
