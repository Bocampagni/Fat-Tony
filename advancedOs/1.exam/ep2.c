#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>

#define DEFAULT_MODE S_IFREG

int mode_flag = DEFAULT_MODE;
int count = 0;

void count_inodes(const char *full_path) {
    struct stat statbuf;
    if (lstat(full_path, &statbuf) != 0) {
        perror("Falha ao pegar o status do arquivo");
        return;
    }
    
    // aplica mascara S_IFMT, via bitwise, para pegar o tipo do arquivo
    int file_type = (statbuf.st_mode & S_IFMT); 
    if (file_type == mode_flag) {
        count++;
    }
}

int walk_dir(const char *path, void (*func)(const char *)) {
    DIR *dirp;
    struct dirent *dp;
    char *p, *full_path;
    int len;

    if ((dirp = opendir(path)) == NULL)
        return (-1);

    len = strlen(path);
    if ((full_path = malloc(len + NAME_MAX + 2)) == NULL) {
        closedir(dirp);
        return (-1);
    }

    memcpy(full_path, path, len);
    p = full_path + len;
    *p++ = '/';

    while ((dp = readdir(dirp)) != NULL) {
        if (strcmp(dp->d_name, ".") == 0 || strcmp(dp->d_name, "..") == 0)
            continue;

        strcpy(p, dp->d_name);
        (*func)(full_path);
    }

    free(full_path);
    closedir(dirp);
    return (0);
}

int main(int argc, char *argv[]) {
    int opt;
    while ((opt = getopt(argc, argv, "rdlbc")) != -1) {
        switch (opt) {
            case 'r': mode_flag = S_IFREG; break;
            case 'd': mode_flag = S_IFDIR; break;
            case 'l': mode_flag = S_IFLNK; break;
            case 'b': mode_flag = S_IFBLK; break;
            case 'c': mode_flag = S_IFCHR; break;
        }
    }

    if (optind == argc) {
        count = 0;
        walk_dir(".", count_inodes);
        printf("Número total de entradas do tipo especificado, em '.': %d\n", count);
    } else {
        for (int index = optind; index < argc; index++) {
            count = 0;
            walk_dir(argv[index], count_inodes);
            printf("Número total de entradas do tipo especificado, em '%s': %d\n", argv[index], count);
        }
    }

    return 0;
}
