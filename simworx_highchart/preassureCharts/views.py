from django.views.generic.base import TemplateView
import pandas as pd
import re

class PxProfundidadeView(TemplateView):
    template_name = 'pCharts/pXprofundidade.html'

    def get_context_data(self, **kwargs):
        # get_context_data: Este é um método fornecido pelo Django que é chamado quando o template precisa de dados para ser renderizado. 
        # Ele permite adicionar dados adicionais ao contexto do template.
        context = super().get_context_data(**kwargs)
        # super().get_context_data(**kwargs): Chama o método get_context_data da classe pai (TemplateView) 
        # para garantir que o contexto básico seja configurado antes de adicionar dados adicionais.
        data = self.parse_txt('preassureCharts/data/PxProf.txt')

        # Criar DataFrame a partir dos dados
        df = pd.DataFrame(data)
        # pd.DataFrame(data): O pandas (pd) é uma biblioteca poderosa para manipulação de dados em Python. Aqui, os dados extraídos do arquivo TXT são convertidos em um DataFrame, 
        # que é uma estrutura de dados tabular, semelhante a uma planilha, onde podemos facilmente manipular e visualizar os dados

        # Adicionar os dados da tabela ao contexto
        context['table_data'] = df.to_dict(orient='records')

        # Adicionar cabeçalhos agrupados ao contexto
        context['column_groups'] = [
            {"title": "Profundidade", "span": 2},  # Abrange "Medida" e "Vertical"
            {"title": "Pressào", "span": 1},     # Abrange Pressões
            {"title": "Efeito", "span": 1},     # Abrange Pressões
            {"title": "Sem Cascalho", "span": 4}, # Abrange dados sem cascalho
            {"title": "Com Cascalho", "span": 4}, # Abrange dados com cascalho
            {"title": "Instante", "span": 1},       # Abrange Tempo
        ]
        context['columns'] = [
            "Medida", "Vertical",
            "Hidrostática", "Cascalhos",
            "Max Surge", "Surge", "Min Swab", "Swab",
            "Max Surge", "Surge", "Min Swab", "Swab",
            "Tempo[s]",
        ]
        return context

    @staticmethod
    def parse_txt(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                if re.match(r"^\s*#|^\s*$", line):  # Ignorar cabeçalhos ou linhas vazias
                    continue

                columns = re.split(r"\s{2,}", line.strip())
                if len(columns) < 12:
                    continue

                data.append({
                    "Medida": float(columns[0]),
                    "Vertical": float(columns[1]),
                    "Hidrostática": float(columns[2]),
                    "Cascalhos": float(columns[3]),
                    "Max Surge (Sem Cascalho)": float(columns[4]),
                    "Surge (Sem Cascalho)": float(columns[5]),
                    "Min Swab (Sem Cascalho)": float(columns[6]),
                    "Swab (Sem Cascalho)": float(columns[7]),
                    "Max Surge (Com Cascalho)": float(columns[8]),
                    "Surge (Com Cascalho)": float(columns[9]),
                    "Min Swab (Com Cascalho)": float(columns[10]),
                    "Swab (Com Cascalho)": float(columns[11]),
                    "Tempo": float(columns[-1]),
                })
        return data

# Perguntar! 
# Posso deixar ponto fixo após a virgulas?
# Qual o melhor tipo de gráfico para esses dados?

class PxTempoView(TemplateView):
    template_name = 'pCharts/pXtempo.html'