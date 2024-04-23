#include <stdio.h>
#include <errno.h>
#include <string.h>


int main()
{
    FILE *pFile;
    pFile = fopen("unexist.ent", "r");
    if (pFile == NULL)
        printf("Error opening file unexist.ent: %s\n", strerror(errno));
    return 0;
}