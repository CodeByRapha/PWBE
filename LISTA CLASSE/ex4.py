class Aluno:
    def __init__(self, nome_aluno, matricula, notas):
        self.nome_aluno = nome_aluno  # nome do aluno
        self.matricula = matricula    # número de matrícula
        self.notas = notas            # lista de notas do aluno
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)  # calcula a média das notas
    
    def verificar_situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"         # aprovado se média for 7 ou mais
        return "Reprovado"            # caso contrário, reprovado

# instanciando um aluno com nome, matrícula e notas
media_Aluno = Aluno("Raphaela Tavares", 2479861, [9, 7.5, 8, 6])

# exibe a média e a situação
print(f"Média: {media_Aluno.calcular_media():.2f}")
print(f"Situação do Aluno: {media_Aluno.verificar_situacao()}")
