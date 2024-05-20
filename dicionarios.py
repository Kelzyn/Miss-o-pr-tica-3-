# Criando o dicionário "meu_dicionario"
meu_dicionario = {
    1: {'linguagem': 'Python'},
    2: {'linguagem': 'Java'},
    3: {'linguagem': 'PHP'}
}

# Imprimindo o conteúdo do dicionário
print("Conteúdo do dicionário 'meu_dicionario':", meu_dicionario)

# Imprimindo o tipo de dados do dicionário
print("Tipo de dados do dicionário:", type(meu_dicionario))

# Imprimindo o valor da chave "linguagem" utilizando o método "get"
print("Valor da chave 'linguagem':", meu_dicionario.get(1).get('linguagem'))

# Imprimindo o tamanho do dicionário
print("Tamanho do dicionário:", len(meu_dicionario))

# Criando um novo dicionário aninhado chamado "dicionario_frutas" utilizando o método "dict"
dicionario_frutas = dict()

# Inserindo os elementos no novo dicionário
dicionario_frutas[1] = {'nome': 'limão', 'tipo': 'ácida'}
dicionario_frutas[2] = {'nome': 'laranja', 'tipo': 'ácida'}
dicionario_frutas[3] = {'nome': 'manga', 'tipo': 'semiácida'}
dicionario_frutas[4] = {'nome': 'maça', 'tipo': 'semiácida'}
dicionario_frutas[5] = {'nome': 'banana', 'tipo': 'doce'}
dicionario_frutas[6] = {'nome': 'mamão', 'tipo': 'doce'}

# Imprimindo o valor das chaves "nome" e "tipo" da chave 1
print("Valor das chaves 'nome' e 'tipo' da chave 1:", dicionario_frutas[1]['nome'], "-", dicionario_frutas[1]['tipo'])

# Imprimindo o valor das chaves "nome" e "tipo" da chave 2
print("Valor das chaves 'nome' e 'tipo' da chave 2:", dicionario_frutas[2]['nome'], "-", dicionario_frutas[2]['tipo'])

# Iterando no dicionário "dicionario_frutas" e imprimindo os valores de todas as chaves "nome" e "tipo"
print("Valores das chaves 'nome' e 'tipo' de todas as frutas:")
for chave, valor in dicionario_frutas.items():
    print("Chave:", chave, "- Nome:", valor['nome'], "- Tipo:", valor['tipo'])