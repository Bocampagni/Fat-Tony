import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_probability_scenario1(target):
    p_4 = 5/6  # Probabilidade de obter valor 4
    p_1 = 1/6  # Probabilidade de obter valor 1
    p_accum = 0
    
    if 4 * 100 < target:
        return 0
    elif 1 * 100 >= target:
        return 1


    for k in range(1, 101):
        if k*4 + (100-k)*1 >= target:
            p_k = (p_4 ** k) * (p_1 ** (100 - k)) * math.comb(100, k)
            p_accum += p_k
        

    return p_accum


def calculate_probability_scenario2(target):
    p_3 = 5/6  # Probabilidade de obter valor 3
    p_6 = 1/6  # Probabilidade de obter valor 6
    p_accum = 0

    if 6 * 100 < target:
        return 0
    elif 3 * 100 >= target:
        return 1
    
    for k in range(1, 101):
        if k*6 + (100-k)*3 >= target:
            p_k = (p_6 ** k) * (p_3 ** (100 - k)) * math.comb(100, k)
            p_accum += p_k

    return p_accum
    


def calculate_probability_scenario3(target):
    p_5 = 3/6  # Probabilidade de obter valor 5
    p_2 = 3/6  # Probabilidade de obter valor 2
    p_accum = 0
    
    if 5 * 100 < target:
        return 0
    elif 2 * 100 >= target:
        return 1
    
    for k in range(1, 101):
        if k*5 + (100-k)*2 >= target:
            p_k = (p_5 ** k) * (p_2 ** (100 - k)) * math.comb(100, k)
            p_accum += p_k

    return p_accum



x_values = np.arange(1, 601)
prob_scenario1 = [calculate_probability_scenario1(x) for x in x_values]
prob_scenario2 = [calculate_probability_scenario2(x) for x in x_values]
prob_scenario3 = [calculate_probability_scenario3(x) for x in x_values]


plt.plot(x_values, prob_scenario1, label='Cinco faces 4, uma face 1', color='red')
plt.plot(x_values, prob_scenario2, label='Cinco faces 3, uma face 6', color='green')
plt.plot(x_values, prob_scenario3, label='Três faces 5, três faces 2', color='blue')
plt.xlabel('Valor de x')
plt.ylabel('P(X >= x)')
plt.title('Probabilidade de acumular valor desejado em dado horizonte de tempo')
plt.legend()
plt.show()

