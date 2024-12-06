from django.views.generic import TemplateView
import re

class PxProfundidadeView(TemplateView):
    template_name = 'pCharts/pXprofundidade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = self.parse_txt('preassureCharts\data\PxProf.txt')

        context['table_data'] = data

        context['table_groups'] = [
            {'title': 'Profundidades [m]', 'span': 2 },
            {'title': 'Pressão', 'span': 1 },
            {'title': 'Efeito', 'span': 1 },
            {'title': 'Pressões Sem Cascalho', 'span': 4 },
            {'title': 'Pressões Com Cascalho', 'span': 4 },
            {'title': 'Instante', 'span': 1 }
        ]

        context['columns'] = [
            'Medida', 'Vertical', 'Hidrostática', 'Cascalho',

            'Max. Surge', 'SURGE', 'Min. Swab', 'SWAB',
            'Max. Surge', 'SURGE', 'Min. Swab', 'SWAB',

            'Tempo[s]'
        ]
        # Criando a lista tvdXp_data
        tvdXp_data = []
        tvdXc_data = []
        for row in data:
            # Criando um par de valores: [Pressão, Profundidade]
            tvdXp_data.append([row['Vertical'], row['Hidrostatica']])
            tvdXc_data.append([row['Vertical'], row['Cascalhos']])
        
        context['tvdXp_data'] = tvdXp_data
        context['tvdXc_data'] = tvdXc_data

        return context

    @staticmethod
    def parse_txt(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                
                # Verifica e ignora se é cabeçalho ou linha vazia!
                if re.match(r"^\s*#|^\s*$", line):
                    continue
                # Divide as colunas usando os espaços como metrica entre os valores
                columns = re.split(r"\s{2,}", line.strip())
                if len(columns) < 12:
                    continue
                # Adicionando dicionário à lista de dados 
                data.append({
                    'Medida': float(columns[0]),
                    'Vertical': float(columns[1]),
                    'Hidrostatica': float(columns[2]),
                    'Cascalhos': float(columns[3]),
                    # Pressões sem Cascalho
                    'Max. Surge (Sem Cascalho)': float(columns[4]),
                    'SURGE (Sem Cascalho)': float(columns[5]),
                    'Min. Swab (Sem Cascalho)': float(columns[6]),
                    'SWAB (Sem Cascalho)': float(columns[7]),
                    # Pressões com Cascalho
                    'Max. Surge (Com Cascalho)': float(columns[8]),
                    'SURGE (Com Cascalho)': float(columns[9]),
                    'Min. Swab (Com Cascalho)': float(columns[10]),
                    'SWAB (Com Cascalho)': float(columns[11]),
                    # Instante
                    'Tempo': float(columns[12])
                })
        # print(data[0])
        return data
    
class PxTempoView(TemplateView):
    template_name = 'pCharts/pXtempo.html'