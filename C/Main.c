// Implementing simple swap function using pointers

#include <stdio.h>

void swap(int *a, int *b) {

    int temp = *a;
    *a = *b;
    *b = temp;

}

int main() {
    int n1 = 5;
    int n2 = 7;
    printf("Before:");
    printf("\nn1 is %d and n2 is %d", n1, n2);

    swap(&n1, &n2);

    printf("\n\nAfter:");
    printf("\nn1 is %d and n2 is %d", n1, n2);

    return 0;
}