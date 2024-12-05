import os
from django.shortcuts import render
import pandas as pd

def index(request):
    # Caminho dinâmico baseado no diretório atual do arquivo views.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'car_sales.csv')

    try:
        # Carrega o CSV
        df = pd.read_csv(csv_path)

        # Verifica se as colunas necessárias estão presentes
        if 'Engine size' not in df.columns or 'Sales in thousands' not in df.columns:
            raise ValueError("CSV não possui as colunas necessárias.")

        # Processa os dados
        rs = df.groupby('Engine size')['Sales in thousands'].agg('sum')
        categories = list(rs.index)
        values = [float(val) for val in rs.values]  # Converte para float nativo

        # Gera tabela
        table_content = df.to_html(index=None)
        table_content = table_content.replace("", "")
        table_content = table_content.replace('class="dataframe"', 'class="table table-striped"')
        table_content = table_content.replace('border="1"', "")

        # Contexto para o template
        context = {"categories": categories, 'values': values, 'table_data': table_content}
        return render(request, 'index.html', context=context)

    except Exception as e:
        # Retorna uma página de erro com a mensagem
        return render(request, 'error.html', {"message": str(e)})
