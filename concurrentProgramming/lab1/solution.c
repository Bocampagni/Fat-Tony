#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define NUM_THREADS 8
#define TAMANHO 10000

int vetor[TAMANHO];

void *square(void *thread_id) {
    long tid = (long)thread_id;
    int start = tid * (TAMANHO / NUM_THREADS);
    int end = (tid + 1) * (TAMANHO / NUM_THREADS);

    printf("Thread %ld: Start = %d, End = %d\n", tid, start, end);

    for (int i = start; i < end; i++) {
        vetor[i] = vetor[i] * vetor[i];
    }

    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    int i;

    for (i = 0; i < TAMANHO; i++) {
        vetor[i] = i + 1;
    }

    for (i = 0; i < NUM_THREADS; i++) {
        if(pthread_create(&threads[i], NULL, square, (void *)i)) {
            printf("--ERRO: pthread_create()\n");
            exit(-1);
        }
    }

    for (i = 0; i < NUM_THREADS; i++) {
        if(pthread_join(threads[i], NULL)) {
            printf("--ERRO: pthread_join() \n");
            exit(-1);
        }
    }
    
    // Teste
    // for (i = 1; i < TAMANHO+1; i++) {
    //     if (i*i != vetor[i-1]) {
    //         printf("Erro na posicao %d\n", i);
    //     }
    // }
    // printf("\n");
    printf("--Thread principal terminou\n");
    pthread_exit(NULL);
}
