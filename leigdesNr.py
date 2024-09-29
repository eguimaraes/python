import numpy as np
import matplotlib.pyplot as plt

# Definindo o número de lançamentos
n_lancamentos = 10000

# Simulando os lançamentos de um dado (valores de 1 a 6)
lancamentos = np.random.randint(1, 7, n_lancamentos)

# Calculando a média acumulada
media_acumulada = np.cumsum(lancamentos) / np.arange(1, n_lancamentos + 1)

# Plotando a média acumulada
plt.figure(figsize=(10, 5))
plt.plot(media_acumulada, label='Média Acumulada')
plt.axhline(y=3.5, color='r', linestyle='--', label='Média Esperada (3.5)')
plt.title('Lei dos Grandes Números: Média Acumulada de Lançamentos de um Dado')
plt.xlabel('Número de Lançamentos')
plt.ylabel('Média Acumulada')
plt.legend()
plt.grid()
plt.show()
