#include <stdio.h>

int main()
{
    int myarr[] = {56,3,6,87,4,13,7,46,3426,37,45};

    int length = sizeof(myarr) / sizeof(myarr[0]);
    //printf("This is length = %d", length);

    // Printing unsorted list 
    printf("Unsorted list:\n");
    for (int i=0; i < length; i++) {
        printf("%d, ", myarr[i]);
    }

    // Bubble sort:
    for (int i=0; i<length; i++) {
        for (int j=0; j<length-i; j++) {
            if (myarr[j] > myarr[j+1]) {
                int tmp = myarr[j+1];
                myarr[j+1] = myarr[j];
                myarr[j] = tmp;

            }
        }
    }

    // Printing sorted list 
    printf("\nSorted list:\n");
    for (int i=0; i < length; i++) {
        printf("%d, ", myarr[i]);
    }

    return 0;
}