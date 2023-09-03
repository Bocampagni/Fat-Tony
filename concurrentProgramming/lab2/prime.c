#include <stdio.h>
#include <pthread.h>
#include <sys/sysinfo.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include "timer.h"


int global_buffer = 0;

struct ThreadArgs {
    int dim;
    int start;
    int end;
};

pthread_mutex_t mutex; 

int ehPrimo(long long int n) {
    int i;
    if (n<=1) return 0;
    if (n==2) return 1;
    if (n%2==0) return 0;
    for (i=3; i<sqrt(n)+1; i+=2)
        if(n%i==0) return 0;
    return 1;
}

void* calculaPrimo(void* args) {
    struct ThreadArgs* threadArgs = (struct ThreadArgs*)args;
    int start = threadArgs->start;
    int end = threadArgs->end;

    for (int i = start; i < end; i++) {
        if (ehPrimo(i)) {
            
            pthread_mutex_lock(&mutex);
            global_buffer += 1;
            pthread_mutex_unlock(&mutex);

        }
    }

    pthread_exit(NULL);
}

int main(int argc, char* argv[]){

    int NUM_THREADS;
    int SETTLED_N;
    
    double inicio, fim, delta;
    
    if (argc < 2) {
        printf("Número de iterações não especificado, utilizando número padrão: %d\n", 10000);
        SETTLED_N = 10000;
    } else {
        SETTLED_N = atoi(argv[1]);
    }
    
    if (argc < 3) {
        printf("Número de threads não especificado. Usando número de threads padrão: %d\n", get_nprocs());
        NUM_THREADS = get_nprocs();
    } else {
        NUM_THREADS = atoi(argv[2]);
    }


    if (SETTLED_N < NUM_THREADS) {
        printf("Número de iterações menor que o número de threads. Reduzindo número de threads para: %d\n", SETTLED_N);
        NUM_THREADS = SETTLED_N;
    }
    
   
    pthread_t threads[NUM_THREADS];
    struct ThreadArgs threadArgs[NUM_THREADS];

    GET_TIME(inicio);
    for (int i = 0; i < NUM_THREADS; i++) {
        threadArgs[i].dim = SETTLED_N;
        threadArgs[i].start = i * (SETTLED_N / NUM_THREADS);
        threadArgs[i].end = (i == NUM_THREADS - 1) ? SETTLED_N : (i + 1) * (SETTLED_N / NUM_THREADS);

        //printf("Criando a thread %d para calcular o primo entre %d e %d.\n", i, threadArgs[i].start, threadArgs[i].end);
        if(pthread_create(&threads[i], NULL, calculaPrimo, &threadArgs[i])){
            printf("Erro ao criar thread %d\n", i);
            return -1;
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        if(pthread_join(threads[i], NULL)){
            printf("Erro ao aguardar thread %d\n", i);
            return -1;
        }
    }
    
    GET_TIME(fim);
    delta = fim - inicio;
    
    printf("A quantidade de números primos entre 0 e %d é: %d\n", SETTLED_N, global_buffer);
    printf("Tempo de execução: %lf para %d threads\n", delta, NUM_THREADS);

    return 0;
}