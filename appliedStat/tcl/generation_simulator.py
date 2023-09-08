from random import randint
import matplotlib.pyplot as plt
import numpy as np

AGES = 10000

def simulador(M):
    generations = []
    for _ in range(AGES):
        coins = [randint(0, 1) for _ in range(M)]
        generations.append(sum(coins))

    plt.subplot(2, 1, 1)
    bins = np.arange(-0.5, M + 1.5, 1)  # Centralize as barras
    plt.hist(generations, bins=bins, rwidth=0.2, align='mid', density=True)
    plt.xlabel('Soma')
    plt.ylabel('Probabilidade')
    plt.title(f'PMF da soma de {M} moedas {AGES} vezes')

    plt.subplot(2, 1, 2)
    plt.hist(generations, cumulative=True, align='mid', density=True, histtype='step')
    plt.xlabel('Soma')
    plt.ylabel('Probabilidade Acumulada')
    plt.title(f'CDF da soma de {M} moedas {AGES} vezes')

    plt.tight_layout()  
    plt.show()

simulador(100)
