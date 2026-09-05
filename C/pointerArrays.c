// Iterating arrays using pointers

#include <stdio.h>

int main() {
    
    int arr[] = {20,43,65,7,62,4};
    int *arrPtr = arr; // like ..= &arr[0]
    int length = sizeof(arr) / sizeof(arr[0]);

    for (int i=0; i<length; i++) {

        printf("%d, ", *(arrPtr + i));
    }

    return 0;

}


