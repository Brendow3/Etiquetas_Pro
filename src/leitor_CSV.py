import pandas as pd

def ler_csv_completo(caminho):
    if not caminho:
        raise ValueError("Nenhum arquivo CSV selecionado.")
    df = pd.read_csv(caminho)
    # Verifique se as colunas essenciais existem
    colunas_necessarias = ['nome', 'categoria', 'preco']
    for coluna in colunas_necessarias:
        if coluna not in df.columns:
            raise ValueError(f"Coluna obrigatória '{coluna}' não encontrada no CSV.")
    return df

def obter_categorias(df):
    return df['categoria'].unique().tolist()

def filtrar_por_categoria(df, categoria):
    return df[df['categoria'] == categoria]
