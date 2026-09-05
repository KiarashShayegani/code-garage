// Fibonacci in C

#include <stdio.h>


int fibo(int n) {

    if (n==1 || n==0) {
        return 1;
    }

    return fibo(n-1) + fibo(n-2);
}

int main() {
    
    int result;
    int choice;
    printf("Enter n to calculate fibo: ");
    scanf("%d", &choice);

    result = fibo(choice);

    printf("Result is: %d", result);

    return 0;
}