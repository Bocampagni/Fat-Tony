#include <stdio.h>
#include <pthread.h>
#include <sys/sysinfo.h>
#include <stdbool.h>
#include <stdlib.h>

pthread_mutex_t mutex;
pthread_cond_t cond;
int state_manager = 0;
int arrived_thread = 0;

struct thread_data
{
    int thread_id;
    int thread_cluster_size;
};

void barreira(int tid, int cluster_size)
{
    pthread_mutex_lock(&mutex);
    if (arrived_thread < cluster_size - 1)
    {
        arrived_thread += 1;
        pthread_cond_wait(&cond, &mutex);
    }
    else
    {
        arrived_thread = 0;
        state_manager += 1;
        printf("\n");
        pthread_cond_broadcast(&cond);
    }
    pthread_mutex_unlock(&mutex);
}

void *show_message(void *thread_data)
{
    struct thread_data *my_data;
    my_data = (struct thread_data *)thread_data;
    int tid = my_data->thread_id;
    int cluster_size = my_data->thread_cluster_size;

    printf("Olá da thread %d \n", tid);
    barreira(tid, cluster_size);

    pthread_mutex_lock(&mutex);
    if (state_manager == 1)
    {
        printf("Que dia bonito %d\n", tid);
    }
    pthread_mutex_unlock(&mutex);

    barreira(tid, cluster_size);

    pthread_mutex_lock(&mutex);
    if (state_manager == 2)
    {
        printf("Até breve %d\n", tid);
    }
    pthread_mutex_unlock(&mutex);
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{

    int NUM_THREADS;

    if (argc < 2)
    {
        printf("Número de threads não especificado. Usando número de threads padrão: %d\n", get_nprocs());
        NUM_THREADS = get_nprocs();
    }
    else
    {
        NUM_THREADS = atoi(argv[1]);
        printf("Número de threads especificado: %d\n\n", NUM_THREADS);
    }

    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond, NULL);

    pthread_t threads[NUM_THREADS];
    struct thread_data thread_data[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++)
    {
        thread_data[i].thread_id = i;
        thread_data[i].thread_cluster_size = NUM_THREADS;
        pthread_create(&threads[i], NULL, show_message, &thread_data[i]);
    }

    for (int i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("\nFIM\n");

    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);

    return 0;
}