import calendar
from datetime import datetime, date

class Calendario:
    def __init__(self):
        # dicionário de feriados fixos no formato 'MM-DD': 'nome do feriado'
        self.feriados = {
            '01-01': 'Ano Novo',
            '04-21': 'Tiradentes',
            '05-01': 'Dia do Trabalho',
            '09-07': 'Independência do Brasil',
            '10-12': 'Nossa Senhora Aparecida',
            '11-02': 'Finados',
            '11-15': 'Proclamação da República',
            '12-25': 'Natal'
        }

    def exibir_mes(self, ano, mes):
        # mostra o calendário do mês em texto
        print(calendar.month(ano, mes))

    def eh_feriado(self, data_str):
        # Verifica se a data (no formato 'YYYY-MM-DD') é feriado
        data = datetime.strptime(data_str, '%Y-%m-%d')
        chave = data.strftime('%m-%d')
        return self.feriados.get(chave, False)

    def diferenca_dias(self, data1_str, data2_str):
        # calcula a diferença de dias entre duas datas ('YYYY-MM-DD')
        d1 = datetime.strptime(data1_str, '%Y-%m-%d').date()
        d2 = datetime.strptime(data2_str, '%Y-%m-%d').date()
        return abs((d2 - d1).days)

c = Calendario()

c.exibir_mes(2025, 6)  # junho de 2025

print(c.eh_feriado('2025-12-25'))  # Natal → "Natal"
print(c.eh_feriado('2025-12-24'))  # não é feriado → Falso

print(c.diferenca_dias('2025-06-01', '2025-06-09'))  # → 8
