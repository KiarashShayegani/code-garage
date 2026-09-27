#include <stdio.h>
#include <stdlib.h>

int *squarer(int n) {
    int *arr = malloc(n * sizeof(int));
    for (int i=0; i<n; i++) {
        arr[i] = (i+1) * (i+1);
    }
    return arr;
}

int main()
{
    int n = 10;
    int *result = squarer(n);
    for(int i=0; i<n; i++) {
        printf("%d \n", result[i]);
    }
    free(result);
    return 0;
}