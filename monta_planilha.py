import pandas as pd
import random
from datetime import datetime, timedelta

# Definindo listas de produtos e seus tipos correspondentes
produtos_tipos = {
    'Óleo': 'alimento',
    'Arroz': 'alimento',
    'Feijão': 'alimento',
    'Macarrão': 'alimento',
    'Açúcar': 'alimento',
    'Café': 'bebida',
    'Leite': 'bebida',
    'Farinha': 'alimento',
    'Sal': 'alimento',
    'Biscoito': 'alimento',
    'Shampoo': 'higiene',
    'Sabonete': 'higiene',
    'Papel Higiênico': 'higiene',
    'Desodorante': 'higiene',
    'Sabão': 'limpeza',
    'Desinfetante': 'limpeza',
    'Álcool': 'limpeza'
}

formas_pagamento = ['PIX', 'Cartão de Crédito', 'Cartão de Débito', 'Dinheiro', 'Voucher']

# Função para gerar uma data aleatória
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Geração de 500 linhas de dados
data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 9, 23)

for i in range(500):
    produto = random.choice(list(produtos_tipos.keys()))
    tipo = produtos_tipos[produto]  # Tipo correspondente ao produto
    quantidade_vendida = random.randint(1, 50)
    preco_unitario = round(random.uniform(1.00, 100.00), 2)
    preco_total = round(quantidade_vendida * preco_unitario, 2)
    forma_pagamento = random.choice(formas_pagamento)
    data_venda = random_date(start_date, end_date).date()
    horario_venda = (datetime.min + timedelta(seconds=random.randint(0, 86399))).time()  # horário aleatório do dia
    
    # Adicionando os dados na lista
    data.append([produto, tipo, quantidade_vendida, f"R$ {preco_unitario}", f"R$ {preco_total}", forma_pagamento, data_venda, horario_venda])

# Criando DataFrame
df = pd.DataFrame(data, columns=['PRODUTO', 'TIPO', 'QUANTIDADE VENDIDA', 'PREÇO UNITÁRIO', 'PREÇO TOTAL', 'FORMA DE PAGAMENTO', 'DATA DA VENDA', 'HORÁRIO DA VENDA'])

# Salvando para um arquivo Excel
df.to_excel('planilha_vendas_exemplo.xlsx', index=False)
