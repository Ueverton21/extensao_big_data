import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados da planilha
df = pd.read_excel('planilha_vendas_exemplo.xlsx')

# Convertendo a coluna de data e hora
df['DATA DA VENDA'] = pd.to_datetime(df['DATA DA VENDA'].astype(str) + ' ' + df['HORÁRIO DA VENDA'].astype(str))
df['DIA DA SEMANA'] = df['DATA DA VENDA'].dt.day_name()
df['HORA DA VENDA'] = df['DATA DA VENDA'].dt.hour

# Remover "R$" das colunas de preço e converter para numérico
df['PREÇO UNITÁRIO'] = df['PREÇO UNITÁRIO'].replace({r'R\$ ': ''}, regex=True).astype(float)
df['PREÇO TOTAL'] = df['PREÇO TOTAL'].replace({r'R\$ ': ''}, regex=True).astype(float)

# Vendas por hora
vendas_por_hora = df.groupby('HORA DA VENDA')['PREÇO TOTAL'].sum()

# Plotando o gráfico de vendas por hora
plt.figure(figsize=(10, 6))
vendas_por_hora.plot(kind='line', marker='o', color='green')
plt.title('Total de Vendas por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(range(0, 24))  # Marcadores de 0 a 23 (horas)
plt.grid(True)
plt.show()
