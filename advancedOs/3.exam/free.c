#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define BUFFER_SIZE 256

void parse_line(const char *line, const char *label, unsigned long *value) {
    if (strncmp(line, label, strlen(label)) == 0) {
        sscanf(line + strlen(label), "%lu", value);
    }
}

unsigned long convert_units(unsigned long kibibytes, char unit) {
    switch (unit) {
        case 'k': return (kibibytes * 1024) / 1000;  // kilobytes
        case 'm': return (kibibytes * 1024) / ( 1000*1000);  // megabytes
        case 'g': return (kibibytes * 1024) / ( 1000*1000*1000);  // gigabytes
        case 't': return (kibibytes * 1024) / ( 1000L*1000L*1000L*1000L);  // terabytes
        case 'p': return (kibibytes * 1024) / ( 1000L*1000L*1000L*1000L*1000L);  // petabytes
        default: return kibibytes;  // default to kibibytes if no valid unit is provided
    }
}

int main(int argc, char *argv[]) {
    char unit = 'd';  // default to kibibytes
    int show_total_line = 0;  // flag for showing the total line
    bool choose_unit = false;
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--kilo") == 0){
            unit = 'k';
            if (choose_unit){
                printf("free: Multiple unit options doesn't make sense.\n");
                return(EXIT_FAILURE);
           }
            choose_unit = true;
        }
        else if (strcmp(argv[i], "--mega") == 0){
            unit = 'm';
            if (choose_unit){
                printf("free: Multiple unit options doesn't make sense.\n");
                return(EXIT_FAILURE);
           }
            choose_unit = true;
        } 
        else if (strcmp(argv[i], "--giga") == 0){
            unit = 'g';
            if (choose_unit){
                printf("free: Multiple unit options doesn't make sense.\n");
                return(EXIT_FAILURE);
           }
            choose_unit = true;
        }
        else if (strcmp(argv[i], "--tera") == 0){
            unit = 't';
            if (choose_unit){
                printf("free: Multiple unit options doesn't make sense.\n");
                return(EXIT_FAILURE);
           }
            choose_unit = true;
        }
        else if (strcmp(argv[i], "--peta") == 0){
            unit = 'p';
            if (choose_unit){
                printf("free: Multiple unit options doesn't make sense.\n");
                return(EXIT_FAILURE);
            }
        }
        else if (strcmp(argv[i], "-t") == 0) show_total_line = 1;
    }

    FILE *file = fopen("/proc/meminfo", "r");
    if (file == NULL) {
        perror("Failed to open /proc/meminfo");
        return 1;
    }

    unsigned long mem_total = 0, mem_free = 0, buffers = 0, cached = 0, swap_total = 0, swap_free = 0, mem_available = 0, shared = 0, sreclaimable = 0;
    char buffer[BUFFER_SIZE];
    while (fgets(buffer, BUFFER_SIZE, file)) {
        parse_line(buffer, "MemTotal:", &mem_total);
        parse_line(buffer, "MemFree:", &mem_free);
        parse_line(buffer, "Buffers:", &buffers);
        parse_line(buffer, "Cached:", &cached);
        parse_line(buffer, "Shmem:", &shared);
        parse_line(buffer, "SwapTotal:", &swap_total);
        parse_line(buffer, "SwapFree:", &swap_free);
        parse_line(buffer, "MemAvailable:", &mem_available);
        parse_line(buffer, "SReclaimable:", &sreclaimable);
    }
    fclose(file);
    unsigned long buff_cache = buffers + cached + sreclaimable;
    unsigned long mem_used = mem_total - mem_free - buff_cache;
    unsigned long swap_used = swap_total - swap_free;

    printf("               total        used        free      shared  buff/cache   available\n");
    printf("Mem:   %13lu%12lu%12lu%12lu%12lu%12lu\n",
           convert_units(mem_total, unit), 
           convert_units(mem_used, unit), 
           convert_units(mem_free, unit), 
           convert_units(shared, unit),
           convert_units(buff_cache, unit), 
           convert_units(mem_available, unit));
    printf("Swap:  %13lu%12lu%12lu\n", 
           convert_units(swap_total, unit), 
           convert_units(swap_used, unit), 
           convert_units(swap_free, unit));

    if (show_total_line) {
        printf("Total: %13lu%12lu%12lu\n", 
               convert_units(mem_total + swap_total, unit), 
               convert_units(mem_used + swap_used, unit), 
               convert_units(mem_free + swap_free, unit));
    }

    return 0;
}