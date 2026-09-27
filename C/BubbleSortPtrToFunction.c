#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int A[], int length, int (*compare)(int, int)) {
    for(int i=0; i<length-1; i++) {
        for(int j=0; j< length - 1 - i; j++) {
            if(compare(A[j], A[j+1]) > 0){
                int temp = A[j+1];
                A[j+1] = A[j];
                A[j] = temp;
            }
        }
    }
}

int INC(int n1, int n2) {
    return (n1>n2) ? 1:-1;
}

int DEC(int n1, int n2) {
    return (n1<n2) ? 1:-1;
}

void print_array(int A[], int length) {
    for(int i=0; i<length; i++) {
        if(i == length) {
            printf("%d", A[i]);
        }
        printf("%d, ", A[i]);
    }
}

int main()
{
    int A[] = {54,7,4627,13789,46,0,213,12, 546};
    int length = sizeof(A) / sizeof(A[0]);

    printf("\nBefore sorting:\n");
    print_array(A, length);

    printf("\n\nBubble sort INC:\n");
    bubble_sort(A, length, INC);
    print_array(A, length);

    printf("\n\nBubble sort DEC:\n");
    bubble_sort(A, length, DEC);
    print_array(A, length);

    return 0;

}