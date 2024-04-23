#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

int isopen(int fd) {
    errno = 0; 
    int flags = fcntl(fd, F_GETFL); //Se o descritor estiver aberto, então ele precisa ter um status, que foi setado pelo open.
    return (flags != -1 || errno != EBADF); // Se ele não estiver aberto, buscar por seu status irá falhar e o retorno será -1. 
}

int main(void) {
    int nopen, fd;

    for (nopen = 0, fd = 0; fd < getdtablesize(); fd++) {
        if (isopen(fd)){
            nopen++;
            printf("O descritor %d está aberto\n", fd);
        }
    }
    printf("Existem %d descritores abertos\n", nopen); // Corrected format string

    return 0;
}
