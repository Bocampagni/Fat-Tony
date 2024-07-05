#include <stdio.h>
#include <stdlib.h>
#include <sys/statvfs.h>

void human_readable_size(unsigned long long size, char *buf) {
    const char *units[] = {"B", "KB", "MB", "GB", "TB"};
    int unit_index = 0;
    double display_size = size;
    
    while (display_size >= 1024 && unit_index < 4) {
        display_size /= 1024;
        unit_index++;
    }
    
    sprintf(buf, "%.2f %s", display_size, units[unit_index]);
}

void print_disk_usage(const char *path) {
    struct statvfs stat;

    if (statvfs(path, &stat) != 0) {
        perror("statvfs");
        return;
    }

    unsigned long long total = stat.f_blocks * stat.f_frsize;
    unsigned long long available = stat.f_bavail * stat.f_frsize;
    unsigned long long used = total - available;

    char total_str[20], used_str[20], available_str[20];
    human_readable_size(total, total_str);
    human_readable_size(used, used_str);
    human_readable_size(available, available_str);

    printf("%-20s %-10s %-10s %-10s %6.2f%%\n", 
           path, total_str, used_str, available_str, 
           (double) used / total * 100);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <path>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    for (int i = 1; i < argc; i++) {
        print_disk_usage(argv[i]);
    }

    return 0;
}

