import pandas as pd
import plotly.express as px 
import plotly.io as pio

df = pd.read_csv("dataset/relatorio_google_ads.csv", skiprows=4)
df = df[df['Dia'] != 'Total']
print(df.dtypes)
print(df.shape)

df['Dia'] = pd.to_datetime(df['Dia'], format='%d/%m/%Y')
print(df.dtypes)
print(df.shape)

df['Custo'] = (
    df['Custo']
    .str.replace('R$ ', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

df['Impr.'] = df['Impr.'].str.replace('.', '', regex=False).astype(int)

print(df['Custo'].dtype )
print(df['Custo'].head())
print(df['Impr.'].dtype)
print(df['Impr.'].head())

df['Custo / conv.'] = (
    df['Custo / conv.']
    .str.replace('R$ ', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
)

df['Custo / conv.'] = pd.to_numeric(df['Custo / conv.'], errors='coerce')

print(df['Custo / conv.'].dtype)
print(df['Custo / conv.'].head(10))

df['CPC méd.'] = (
    df['CPC méd.']
    .str.replace('R$ ', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
)

df['CPC méd.'] = pd.to_numeric(df['CPC méd.'], errors='coerce')

print(df['CPC méd.'].dtype)
print(df['CPC méd.'].head(10))

df['CTR'] = (
    df['CTR']
    .str.replace('%', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
)
df['CTR'] = pd.to_numeric(df['CTR'], errors='coerce')

print(df['CTR'].dtype)
print(df['CTR'].head(10))

df['Taxa de conv.'] = (
    df['Taxa de conv.']
    .str.replace('%', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
)
df['Taxa de conv.'] = pd.to_numeric(df['Taxa de conv.'], errors='coerce')

print(df['Taxa de conv.'].dtype)
print(df['Taxa de conv.'].head(10))

funil_campanha = df.groupby('Campanha')[['Cliques', 'Conversões']].sum()
print(funil_campanha)

funil_campanha['taxa_conversao'] = funil_campanha['Conversões'] / funil_campanha['Cliques'] * 100
print(funil_campanha)

funil_campanha = funil_campanha.reset_index()

fig = px.bar(funil_campanha, x='Campanha', y='taxa_conversao')

#fig.show()
fig.write_html("grafico_taxa_conversao.html")
#pio.renderers.default = "browser"