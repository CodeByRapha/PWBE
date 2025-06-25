class Tarefa:
    def __init__(self, titulo, prioridade, data_venc, status, categoria):
        self.titulo = titulo
        self.prioridade = prioridade  # 1=alta,2=media,3=baixa
        self.data_venc = data_venc
        self.status = status          # 'pendente', 'andamento', 'concluida'
        self.categoria = categoria

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def listar(self, status=None, prioridade=None):
        return [t for t in self.tarefas 
                if (status is None or t.status == status) and 
                   (prioridade is None or t.prioridade == prioridade)]

    def remover(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)

# Exemplo
g = GerenciadorTarefas()
t1 = Tarefa("Estudar", 1, "2025-06-30", "pendente", "Estudos")
t2 = Tarefa("Comprar", 3, "2025-07-05", "andamento", "Pessoal")
g.adicionar(t1)
g.adicionar(t2)

pendentes = g.listar(status="pendente")
for t in pendentes:
    print(t.titulo, t.status)
