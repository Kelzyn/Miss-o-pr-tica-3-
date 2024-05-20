
from operacoes import calcular_media, verificar_reprovacao, identificar_aluno_reprovado

# Dados dos alunos e notas de cada bimestre
dados_alunos = [
    {"nome": "Maria", "matricula": 1001, "notas": [7, 6, 5, 8]},
    {"nome": "João", "matricula": 1002, "notas": [5, 4, 6, 7]},
    {"nome": "Ana", "matricula": 1003, "notas": [6, 7, 6, 5]}
]

# Calcular a média de cada aluno
for aluno in dados_alunos:
    aluno["media"] = calcular_media(aluno["notas"])

# Verificar se um aluno foi reprovado e identificar quem foi reprovado
alunos_reprovados = []
for aluno in dados_alunos:
    if verificar_reprovacao(aluno["media"]):
        alunos_reprovados.append(aluno["matricula"])

# Imprimir os dados dos alunos reprovados
for aluno in dados_alunos:
    if aluno["matricula"] in alunos_reprovados:
        print(identificar_aluno_reprovado(dados_alunos, alunos_reprovados))