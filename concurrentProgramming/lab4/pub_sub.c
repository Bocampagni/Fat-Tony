#include <stdio.h>
#include <stdlib.h>
#include "list_int.h"
#include <pthread.h>
#include "timer.h"

#define QTDE_OPS 10000000 
#define QTDE_INI 100 
#define MAX_VALUE 100 

struct list_node_s* head_p = NULL;
int nthreads;

pthread_mutex_t mutex;

pthread_cond_t cond_write;

pthread_cond_t cond_read;


int readers = 0;
int writers = 0;

void writer() {
    pthread_mutex_lock(&mutex);
    while ((readers > 0) || (writers > 0)) {
        pthread_cond_wait(&cond_write, &mutex);
    }
    writers++;
    pthread_mutex_unlock(&mutex);    
}


void exit_writer() {
    pthread_mutex_lock(&mutex);
    writers--;
    
    pthread_cond_signal(&cond_write);
    pthread_cond_broadcast(&cond_read);
    pthread_mutex_unlock(&mutex);

}

void reader() {
    pthread_mutex_lock(&mutex);
    while (writers > 0) {
        pthread_cond_wait(&cond_read, &mutex);
    }

    readers++;
    pthread_mutex_unlock(&mutex);
}

void exit_reader() {
    pthread_mutex_lock(&mutex);
    readers--;
    if (readers == 0) {
        pthread_cond_broadcast(&cond_write);
    }
    pthread_mutex_unlock(&mutex);
}



void* tarefa(void* arg) {
   long int id = (long int) arg;
   int op;
   int in, out, read; 
   in=out=read = 0; 

   for(long int i=id; i<QTDE_OPS; i+=nthreads) {
      op = rand() % 100;
      if(op<98) {
        reader();
         Member(i%MAX_VALUE, head_p);   
        exit_reader();
     read++;
      } else if(98<=op && op<99) {
        writer();
         Insert(i%MAX_VALUE, &head_p);  
        exit_writer();
	 in++;
      } else if(op>=99) {
        writer();
         Delete(i%MAX_VALUE, &head_p);  
        exit_writer();
	 out++;
      }
   }

   
   printf("Thread %ld: in=%d out=%d read=%d\n", id, in, out, read);
   pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
   pthread_t *tid;
   double ini, fim, delta;
   
   if(argc<2) {
      printf("Digite: %s <numero de threads>\n", argv[0]); return 1;
   }
   nthreads = atoi(argv[1]);

   for(int i=0; i<QTDE_INI; i++)
      Insert(i%MAX_VALUE, &head_p);  
   
   GET_TIME(ini);

   tid = malloc(sizeof(pthread_t)*nthreads);
   if(tid==NULL) {  
      printf("--ERRO: malloc()\n"); return 2;
   }

   for(long int i=0; i<nthreads; i++) {
      if(pthread_create(tid+i, NULL, tarefa, (void*) i)) {
         printf("--ERRO: pthread_create()\n"); return 3;
      }
   }
   
   for(int i=0; i<nthreads; i++) {
      if(pthread_join(*(tid+i), NULL)) {
         printf("--ERRO: pthread_join()\n"); return 4;
      }
   }

   GET_TIME(fim);
   delta = fim-ini;
   printf("Tempo: %lf\n", delta);

   free(tid);
   Free_list(&head_p);

   return 0;
}  /* main */