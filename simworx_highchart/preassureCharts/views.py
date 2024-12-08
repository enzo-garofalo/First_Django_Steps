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
        
        # Criando listas para as séries
        total_max_surge_com = 0
        total_max_surge_sem = 0

        total_surge_com = 0
        total_surge_sem = 0

        total_min_swab_com = 0
        total_min_swab_sem = 0
 
        total_swab_com = 0
        total_swab_sem = 0
   
        for row in data:
            # Criando um par de valores: [Pressão, Profundidade]
            tvdXp_data.append([row['Vertical'], row['Hidrostatica']])
            tvdXc_data.append([row['Vertical'], row['Cascalhos']])
            # Criando pares de valores, com cascalho e sem cascalho
            total_max_surge_com += row['Max. Surge (Com Cascalho)']
            total_max_surge_sem += row['Max. Surge (Sem Cascalho)']

            total_surge_com += row['SURGE (Com Cascalho)']
            total_surge_sem += row['SURGE (Sem Cascalho)']

            total_min_swab_com += row['Min. Swab (Com Cascalho)']
            total_min_swab_sem += row['Min. Swab (Sem Cascalho)']

            total_swab_com += row['SWAB (Com Cascalho)']
            total_swab_sem += row['SWAB (Sem Cascalho)']
        
        context['tvdXp_data'] = tvdXp_data
        context['tvdXc_data'] = tvdXc_data
        context['chart_data'] = {
            'max_surge': [total_max_surge_com//len(data), total_max_surge_sem//len(data)],
            'surge': [total_surge_com//len(data), total_surge_sem//len(data)],
            'min_swab': [total_min_swab_com//len(data), total_min_swab_sem//len(data)],
            'swab': [total_swab_com//len(data), total_swab_sem//len(data)],
        }

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Configurando cabeçalho
        context['table_titles'] = [
            {'title' : '', 'span' : 1},
            {'title' : 'Fluido SEM cascalho', 'span' : 4},
            {'title' : 'Fluido COM cascalho', 'span' : 4}
        ]
        # Configurando titulo das colunas
        context['columns'] = [
            'Tempo [S]',
            'Surge Sapata', 'Surge Fundo', 'Swab Sapata', 'Swab Fundo',
            'Surge Sapata', 'Surge Fundo', 'Swab Sapata', 'Swab Fundo'
        ]

            
        # Parseando dados

        data = self.parse_txt('preassureCharts\data\Pxtempo.txt')
        context['table_data'] = data
        
        # Configurando chart
        surge_sapata_sem = []
        surge_fundo_sem  = []
        swab_sapata_sem  = []
        swab_fundo_sem   = []

        surge_sapata_com = []
        surge_fundo_com = []
        swab_sapata_com = []
        swab_fundo_com = []

        for row in data:
            surge_sapata_sem.append([row['tempo'], row['surge sapata sem cascalho']]),
            surge_fundo_sem.append([row['tempo'], row['surge fundo sem cascalho']]),
            swab_sapata_sem.append([row['tempo'], row['swab sapata sem cascalho']])
            swab_fundo_sem.append([row['tempo'], row['swab fundo sem cascalho']])
  
            surge_sapata_com.append([row['tempo'], row['surge sapata com cascalho']]),
            surge_fundo_com.append([row['tempo'], row['surge fundo com cascalho']]),
            swab_sapata_com.append([row['tempo'], row['swab sapata com cascalho']])
            swab_fundo_com.append([row['tempo'], row['swab fundo com cascalho']])
        
        context['surge_sapata_sem'] = surge_sapata_sem
        context['surge_fundo_sem'] = surge_fundo_sem
        context['swab_sapata_sem'] = swab_sapata_sem
        context['swab_fundo_sem'] = swab_fundo_sem 
        
        context['surge_sapata_com'] = surge_sapata_com
        context['surge_fundo_com'] = surge_fundo_com
        context['swab_sapata_com'] = swab_sapata_com
        context['swab_fundo_com'] = swab_fundo_com 

        return context

    @staticmethod
    def parse_txt(file_path):

        data = []

        with open(file_path, 'r') as file:
            for line in file:
                if re.match(r'\s*#|\s$', line):
                    continue

                columns = re.split(r'\s{2,}', line.strip())
                data.append({
                    'tempo': float(columns[0]),

                    'surge sapata sem cascalho' : float(columns[1]), 
                    'surge fundo sem cascalho' : float(columns[2]), 
                    'swab sapata sem cascalho' : float(columns[3]), 
                    'swab fundo sem cascalho' : float(columns[4]),

                    'surge sapata com cascalho' : float(columns[5]), 
                    'surge fundo com cascalho' : float(columns[6]), 
                    'swab sapata com cascalho' : float(columns[7]), 
                    'swab fundo com cascalho' : float(columns[8])
                })

        return data