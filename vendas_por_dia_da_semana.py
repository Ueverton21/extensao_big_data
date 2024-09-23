import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('planilha_vendas_exemplo.xlsx')

# Convertendo a coluna de data e hora
df['DATA DA VENDA'] = pd.to_datetime(df['DATA DA VENDA'].astype(str) + ' ' + df['HORÁRIO DA VENDA'].astype(str))
df['DIA DA SEMANA'] = df['DATA DA VENDA'].dt.day_name()

# Traduzir dias da semana para português
dias_semana_traduzidos = {
    'Monday': 'segunda-feira',
    'Tuesday': 'terça-feira',
    'Wednesday': 'quarta-feira',
    'Thursday': 'quinta-feira',
    'Friday': 'sexta-feira',
    'Saturday': 'sábado',
    'Sunday': 'domingo'
}

df['DIA DA SEMANA'] = df['DIA DA SEMANA'].replace(dias_semana_traduzidos)

# Remover "R$" das colunas de preço e converter para numérico
df['PREÇO UNITÁRIO'] = df['PREÇO UNITÁRIO'].replace({r'R\$ ': ''}, regex=True).astype(float)
df['PREÇO TOTAL'] = df['PREÇO TOTAL'].replace({r'R\$ ': ''}, regex=True).astype(float)

# Vendas por dia da semana
vendas_por_dia = df.groupby('DIA DA SEMANA')['PREÇO TOTAL'].sum().reindex(['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo'])

plt.figure(figsize=(10, 6))
vendas_por_dia.plot(kind='bar', color='lightcoral')
plt.title('Total de Vendas por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.show()