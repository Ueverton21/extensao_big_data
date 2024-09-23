import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('planilha_vendas_exemplo.xlsx')

# Convertendo a coluna de data e hora
df['DATA DA VENDA'] = pd.to_datetime(df['DATA DA VENDA'].astype(str) + ' ' + df['HORÁRIO DA VENDA'].astype(str))
df['DIA DA SEMANA'] = df['DATA DA VENDA'].dt.day_name()
df['HORA DA VENDA'] = df['DATA DA VENDA'].dt.hour

# Total de vendas por tipo de produto
vendas_por_tipo = df.groupby('TIPO')['PREÇO TOTAL'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(vendas_por_tipo['TIPO'], vendas_por_tipo['PREÇO TOTAL'], color='skyblue')
plt.title('Total de Vendas por Tipo de Produto')
plt.xlabel('Tipo de Produto')
plt.ylabel('Total de Vendas (R$)')
plt.show()