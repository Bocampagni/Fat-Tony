#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include <sys/types.h>
#include <dirent.h>
#include <string.h>

#define LOG_FILE "~/zombie.log"
#define EVER ;;

void log_zombies();
void daemonize();
void handle_sigterm(int sig);

int main(int argc, char *argv[]) {
    int interval;

    if (argc != 2 || (interval = atoi(argv[1])) <= 0) {
        fprintf(stderr, "Uso: %s <intervalo_em_segundos>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    daemonize();

    signal(SIGTERM, handle_sigterm);
    signal(SIGCHLD, SIG_IGN); // Ignorar sinais de filho

    for (EVER) {
        log_zombies();
        sleep(interval);
    }

    return 0;
}

void daemonize() {
    pid_t pid, sid;

    // Fork para criar um novo processo
    pid = fork();
    if (pid < 0) {
        exit(EXIT_FAILURE);
    }
    // Encerrar o processo pai
    if (pid > 0) {
        exit(EXIT_SUCCESS);
    }

    // Criar um novo SID para o processo filho
    sid = setsid();
    if (sid < 0) {
        exit(EXIT_FAILURE);
    }

    // Mudar diretório de trabalho
    if ((chdir("/")) < 0) {
        exit(EXIT_FAILURE);
    }

    // Fechar os descritores de arquivo padrão
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
}

void log_zombies() {
    FILE *log_file;
    DIR *proc_dir;
    struct dirent *entry;
    char path[256], line[256];
    FILE *status_file;

    log_file = fopen(LOG_FILE, "a");
    if (!log_file) {
        exit(EXIT_FAILURE);
    }

    proc_dir = opendir("/proc");
    if (!proc_dir) {
        fclose(log_file);
        exit(EXIT_FAILURE);
    }

    fprintf(log_file, "==========================================\n");
    fprintf(log_file, "PID       PPID         Nome do Programa\n");
    fprintf(log_file, "==========================================\n");

    while ((entry = readdir(proc_dir)) != NULL) {
        if (entry->d_type == DT_DIR && isdigit(entry->d_name[0])) {
            snprintf(path, sizeof(path), "/proc/%s/status", entry->d_name);
            status_file = fopen(path, "r");
            if (status_file) {
                int pid = -1, ppid = -1;
                char comm[256] = "", state[256] = "";
                while (fgets(line, sizeof(line), status_file)) {
                    if (sscanf(line, "Pid:\t%d", &pid) == 1) {}
                    if (sscanf(line, "PPid:\t%d", &ppid) == 1) {}
                    if (sscanf(line, "Name:\t%s", comm) == 1) {}
                    if (sscanf(line, "State:\t%s", state) == 1) {}
                }
                fclose(status_file);
                if (strcmp(state, "Z") == 0) {
                    fprintf(log_file, "%-10d %-10d %s\n", pid, ppid, comm);
                }
            }
        }
    }

    fprintf(log_file, "==========================================\n");

    closedir(proc_dir);
    fclose(log_file);
}

void handle_sigterm(int sig) {
    FILE *log_file = fopen(LOG_FILE, "a");
    if (log_file) {
        fprintf(log_file, "Daemon finalizado\n");
        fclose(log_file);
    }
    exit(EXIT_SUCCESS);
}

