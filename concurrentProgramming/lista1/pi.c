// Placeholder


#include <stdio.h>
#include <pthread.h>
#include <sys/sysinfo.h>
#include <stdbool.h>
#include <stdlib.h>

#define NUM_THREADS 10

struct ThreadArgs {
    int steps;
    int start;
    int end;
};

double piSequencial (int start, int end) {
    double soma = 0.0, fator = 1.0;
    long long i;
    for (i = start; i < end; i++) {
    soma = soma + fator/(2*i+1);
    fator = -fator;
    }
    return 4.0 * soma;
}

void* thread_wrapper(void* args) {
    struct ThreadArgs* threadArgs = (struct ThreadArgs*)args;
    int steps = threadArgs->steps;
    int start = threadArgs->start;
    int end = threadArgs->end;


    double* pi = (double*) malloc(sizeof(double));
    *pi = piSequencial(start, end);
    pthread_exit((void*)pi);
} 

int main() {
    long long n = 100000;
    int i;
    double pi = 0.0;

    pthread_t threads[NUM_THREADS];
    struct ThreadArgs threadArgs[NUM_THREADS];

    for (i = 0; i < NUM_THREADS; i++) {
        long N_STEP = n/NUM_THREADS;
        threadArgs[i].steps = N_STEP; 
        threadArgs[i].start = i * N_STEP;
        threadArgs[i].end = (i + 1) * N_STEP;

        printf("Criando a thread %d para calcular a linha %d até a linha %d.\n", i, threadArgs[i].start, threadArgs[i].end);
        if (pthread_create(&threads[i], NULL, thread_wrapper, (void*) &threadArgs[i])){
            printf("Erro ao criar a thread %d.\n", i);
            return -1;
        }
    }

    for (i = 0; i < NUM_THREADS; i++) {
        double* piThread;
        if(pthread_join(threads[i], (void**)&piThread)){
            printf("Erro ao aguardar a thread %d.\n", i);
            return -1;
        }
        pi += *piThread;
        free(piThread);
    }

    printf("pi = %f\n", pi);
    return 0;
}