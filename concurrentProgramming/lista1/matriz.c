#include <stdio.h>
#include <pthread.h>
#include <sys/sysinfo.h>

#define N 1000 // N igual à dimensão da matriz
#define NUM_THREADS get_nprocs() // Número de threads (ajuste conforme o número de unidades de processamento)

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

int main() {
    int i, j;
    // Inicialize as matrizes a e b (...)
    
    // Preencha as matrizes a e b com valores aleatórios entre 0 e 1
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if ((i + j) % 2 == 0) {
                a[i][j] = 1;
                b[i][j] = 3;
            } else {
                a[i][j] = 7;
                b[i][j] = 2;
            }
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
        pthread_create(&threads[i], NULL, calculaElementoMatriz, &threadArgs[i]);
    }

    // Aguarde as threads terminarem
    for (i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }


    // Testar se a matriz C está correta
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            float soma = 0.0;
            for (int k = 0; k < N; k++) {
                soma = a[i][k] * b[k][j];
                if (soma != c[i][j]) {
                   printf("Soma = %f, C[%d][%d] = %f\n", soma, i, j, c[i][j]);
                }
            }
        }
    }

    return 0;
}