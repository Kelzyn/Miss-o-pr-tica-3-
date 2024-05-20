
def calcular_media(notas):
    """Calcula a média das notas dos 4 bimestres de um aluno."""
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """Verifica se um aluno foi reprovado com base em sua média."""
    return media < 6

def identificar_aluno_reprovado(dados_alunos, matriculas_reprovadas):
    """Identifica e retorna os dados do aluno reprovado."""
    for aluno in dados_alunos:
        if aluno["matricula"] in matriculas_reprovadas:
            return f'Aluno Reprovado: {aluno["nome"]} - Matrícula: {aluno["matricula"]} - Média Final: {aluno["media"]}'