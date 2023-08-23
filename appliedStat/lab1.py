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


def calculate_probability_scenario2(x):
    p_3 = 5/6  # Probabilidade de obter valor 3
    p_6 = 1/6  # Probabilidade de obter valor 6
    p_accum = 0
    for k in range(x, 101):
        p_k = (p_3 ** k) * (p_6 ** (100 - k)) * math.comb(100, k)
        p_accum += p_k
    return p_accum


def calculate_probability_scenario3(x):
    p_5 = 3/6  # Probabilidade de obter valor 5
    p_2 = 3/6  # Probabilidade de obter valor 2
    p_accum = 0
    for k in range(x, 101):
        p_k = (p_5 ** k) * (p_2 ** (100 - k)) * math.comb(100, k)
        p_accum += p_k
    return p_accum



x_values = np.arange(1, 601)
prob_scenario1 = [calculate_probability_scenario1(x) for x in x_values]
#prob_scenario2 = [calculate_probability_scenario2(x) for x in x_values]
#prob_scenario3 = [calculate_probability_scenario3(x) for x in x_values]
print(list(np.around(prob_scenario1,2)))