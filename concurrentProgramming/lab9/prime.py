import math
import time
import sys
from multiprocessing.pool import Pool


def prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    curr_sqrt = int(math.sqrt(n) + 1)
    for i in range(3, curr_sqrt, 2):
        if n % i == 0:
            return 0
    
    return 1

if __name__ == '__main__':
    N = 1000 # Tamanho da entrada dada pelo usuario

    params = sys.argv
    if len(params) == 1:
        print("error: python3 prime.py <prime lenght>, i.e python3 prime.py 100")
        exit(0)
    
    N = int(params[1])

    start = time.time()
    pool = Pool() # Instancia do objeto Pool

    numbers = list(range(N))
    
    results = pool.map(prime, numbers)

    print('Number of primes found:', sum(results))    
    end = time.time()
    print('work took {} seconds'.format(end - start))
