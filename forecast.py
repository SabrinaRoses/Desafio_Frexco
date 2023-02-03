# Estruture um Script em Python que calcule a previsão de demanda para os próximos 5 dias do item.
# Importando bibliotecas
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

#carregando arquivo de dados.
df = pd.read_excel('Dados.xlsx')

#Realizando previsão para os proximos 5 dias
forecast = ExponentialSmoothing(df['Vendas']).fit().forecast(5)

#Titulo
plt.title('Previsão de Demanda - 5 dias', fontsize = 14)
plt.xlabel("Período - Dia ", fontsize = 12)
plt.ylabel('Vendas Diárias', fontsize = 12)

#Exibição gráfica (Linhas)
plt.plot(df['Vendas'], label = 'Histórico')
plt.plot(forecast, label='Previsão')
plt.legend()
plt.show()
