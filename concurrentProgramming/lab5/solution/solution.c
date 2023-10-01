#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 1000
#define SENTENCE_SIZE 1000

sem_t condt2;
sem_t mutexGeral;

int head_p = 0;
int nthreads;
char buffer[BUFFER_SIZE][SENTENCE_SIZE];

void init_buffer()
{
    for (int i = 0; i < BUFFER_SIZE; i++)
    {
        strcpy(buffer[i], "0");
    }
}

int Retira(int id)
{
    char *item;
    static int out = 0;

    sem_wait(&condt2);
    sem_wait(&mutexGeral);

    item = buffer[out];
    if (strcmp(item, "0") == 0)
    {
        sem_post(&mutexGeral);
        sem_post(&condt2);
        pthread_exit(NULL);
    }

    printf("Consumidor[%d]: %s", id, item);

    strcpy(buffer[out], "");
    out = (out + 1) % BUFFER_SIZE;

    sem_post(&mutexGeral);
    sem_post(&condt2);
}

void *consumidor(void *arg)
{
    long id = (long)(arg);
    while (1)
    {
        Retira(id);

        sleep(1);
    }
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{

    pthread_t *tid;

    sem_init(&mutexGeral, 0, 1);
    sem_init(&condt2, 0, 0);
    init_buffer();

    // Leitura dos parâmemtros via CLI
    if (argc < 3)
    {
        printf("Digite: %s <numero de threads> <nome do arquivo>\n", argv[0]);
        return 1;
    }
    nthreads = atoi(argv[1]);
    char *nome_arquivo = argv[2];

    // Leitura do arquivo
    FILE *arq;
    arq = fopen(nome_arquivo, "r");
    if (arq == NULL)
    {
        printf("Erro ao abrir o arquivo\n");
        return 1;
    }

    tid = (pthread_t *)malloc(sizeof(pthread_t) * nthreads);

    if (tid == NULL)
    {
        printf("Erro ao alocar memória para as threads\n");
        return 1;
    }
    // Criação dos subscribers (threads)
    for (long i = 0; i < nthreads; i++)
    {
        if (pthread_create(&tid[i], NULL, consumidor, (void *)(i)))
        {
            printf("Erro ao criar a thread %ld\n", i);
            return -1;
        }
    }

    int i = 0;
    char sentence[SENTENCE_SIZE];
    while (fgets(sentence, sizeof(sentence), arq) != NULL && i < BUFFER_SIZE)
    {
        strcpy(buffer[i], sentence);
        i++;
    }

    sem_post(&condt2); // Permite leitura

    for (int i = 0; i < nthreads; i++)
    {
        pthread_join(tid[i], NULL);
    }
    
    fclose(arq);
    free(tid);
    return 0;
}