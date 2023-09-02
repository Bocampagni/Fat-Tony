#include <stdio.h>
#include <pthread.h>
#include <sys/sysinfo.h>
#include <stdbool.h>

#define N 100 // N igual à dimensão da matriz
#define NUM_THREADS 10 //get_nprocs(), não foi utilizado porque no meu caso retorna 12, o que implica na necessidade de tratar o restante do número de linhas, devido ao fato do N não ser divisível por 12.

float a[N][N], b[N][N], c[N][N];

// Estrutura para passar argumentos para a função de thread
struct ThreadArgs {
    int dim;
    int start_row;
    int end_row;
};

// Função para calcular uma parte da matriz C
void* calculaElementoMatriz(void* args) {
    struct ThreadArgs* threadArgs = (struct ThreadArgs*)args;
    int dim = threadArgs->dim;
    int start_row = threadArgs->start_row;
    int end_row = threadArgs->end_row;

    int i, j, k, soma;
    
    for (i = start_row; i < end_row; i++) {
        for (j = 0; j < dim; j++) {
            soma = 0.0;
            for (k = 0; k < dim; k++) {
                soma += a[i][k] * b[k][j];
            }
            c[i][j] = soma;
        }
    }

    pthread_exit(NULL);
}

bool verificarMatrizC() {
    int i, j, k;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            float soma = 0.0;
            for (k = 0; k < N; k++) {
                soma += a[i][k] * b[k][j];
            }
            if (c[i][j] != soma) {
                printf("c[%d][%d] = %f != %f = soma\n", i, j, c[i][j], soma);
                return false; // Se os valores não coincidirem, a verificação falha
            }
        }
    }
    return true; // Se a verificação passar, retorna verdadeiro
}

int main() {
    int i, j;
    // Inicialize as matrizes a e b (...)
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
                a[i][j] = i+j;
                b[i][j] = 2*i+j;
        }
    }

    pthread_t threads[NUM_THREADS];
    struct ThreadArgs threadArgs[NUM_THREADS];
    
    int rows_per_thread = N / NUM_THREADS;

    // Crie e execute as threads
    for (i = 0; i < NUM_THREADS; i++) {
        threadArgs[i].dim = N;
        threadArgs[i].start_row = i * rows_per_thread;
        threadArgs[i].end_row = (i + 1) * rows_per_thread;

        printf("Criando a thread %d para calcular a linha %d até a linha %d.\n", i, threadArgs[i].start_row, threadArgs[i].end_row);
        if(pthread_create(&threads[i], NULL, calculaElementoMatriz, &threadArgs[i])){
            printf("Erro ao criar a thread %d.\n", i);
            return -1;
        }
    }

    // Aguarde as threads terminarem
    for (i = 0; i < NUM_THREADS; i++) {
        if(pthread_join(threads[i], NULL)){
            printf("Erro ao aguardar a thread %d.\n", i);
            return -1;
        }
    }

    // Verifique se a matriz C foi calculada corretamente
    if (verificarMatrizC()) {
        printf("A matriz C foi calculada corretamente.\n");
    } else {
        printf("A matriz C não foi calculada corretamente.\n");
    }

    return 0;
}