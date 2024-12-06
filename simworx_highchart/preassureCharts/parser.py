import re

def parse_txt(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Ignorar linhas de cabeçalho ou vazias
            if re.match(r"^\s*#|^\s*$", line):
                continue
            
            # Dividir os valores na linha, baseando-se no espaçamento
            columns = re.split(r"\s{2,}", line.strip())
            if len(columns) < 12:  # Garantir que há colunas suficientes
                continue
            
            data.append({
                "profundidade": float(columns[0]),
                "pressao_hidrostatica": float(columns[2]),
                "pressao_cascalho": float(columns[3]),
                "tempo": float(columns[-1])
            })
    return data

# Exemplo de uso
file_path = '/mnt/data/PxProf.txt'
parsed_data = parse_txt(file_path)
