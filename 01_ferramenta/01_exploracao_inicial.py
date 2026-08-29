import pandas as pd
import matplotlib.pyplot as plt

# CARREGAR DADOS 
df = pd.read_csv("dataset/campanhas_ecommerce_v2.csv")

#AJUSTE INICIAL DE TIPO DE DADOS 
df['data'] = pd.to_datetime(df['data'])

#INSPEÇÃO INICIAL 
print("--- Diagnóstico Inicial")
print("Tipo de Dados:\n", df.dtypes)
print("Formato Inicial (linhas, colunas):", df.shape)
print("Período:", df['data'].min(), "até", df['data'].max())
print("Nulos por coluna:\n",df.isnull().sum())
print("Linhas Duplicadas:\n", df[df.duplicated(keep=False)])

# LIMPEZA E TRATAMENTO 

# Step A: Remover duplicadas primeiro 
df = df.drop_duplicates()
print("\n Formato após remover duplacadas:",df.shape)

# Step B: Preencher valores nulos de "gasto" pela média da respectiva campanha
df['gasto'] = df.groupby('campanha')['gasto'].transform(lambda x: x.fillna(x.mean()))
print("Nulos após tratamento:\n", df.isnull().sum())

# 3. CÁLCULO DE MÉTRICAS DERIVADAS E AGRUPAMENTOS

# Calcular ROAS no nível de linha (após ter limpo nulos e duplicatas)
df['roas'] = df['receita'] / df['gasto']
print("\n Primeiras linhas com a coluna ROAS:")
print(df.head())

# Agrupar por campanha
agrupado = df.groupby('campanha')[['gasto', 'receita']].sum()

# Calcular o ROAS consolidado do agrupado (Receita Total / Gasto Total)
agrupado['roas'] = agrupado['receita'] / agrupado['gasto']

print("\n Métricas Consolidadas por Campanha")
print(agrupado)

print(df.loc[df['gasto'].idxmax()])

df_remarketing_google = df[(df['campanha'] == 'Remarketing - Carrinho Abandonado') & (df['canal'] == 'Google Ads')]
print(df_remarketing_google.shape)

df_remarketing_google = df_remarketing_google.sort_values('data')
print(df_remarketing_google[['data', 'cliques', 'conversoes', 'receita']])

# Filtra apenas o intervalo de 01 a 31 de julho
df_julho = df_remarketing_google[
    df_remarketing_google['data'].between ('2026-07-01', '2026-07-31')
]

print(df_julho[['data', 'cliques', 'conversoes', 'receita']].to_string())

# Prepara o "tamanho da tela" antes de desenhar
plt.figure(figsize=(10,5))

# Desenha cada linha (uma por vez, mesma "tela")
plt.plot(df_julho['data'], df_julho['cliques'], label= 'Cliques')
plt.plot(df_julho['data'], df_julho['conversoes'], label='Conversões')

# Adiciona título e nomes dos eixos
plt.title('Cliques e Conversões - Remarketing Google Ads - Julho/2026')
plt.xlabel('Data')
plt.ylabel('Quantiidae')

# Ativa a legenda (usa os "label" que você definiu no passo 2)
plt.legend()

# Ajustes visuais finais 
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


