#include <stdio.h>

long factorial(int n) {

    long int fact = 1;
    if (n == 0 || n ==1) {
        return 1;
    } else if (n < 0) {
        printf("No negative numbers bitch!!\n");
        return -1;
    } else {
        fact = n * factorial(n-1);
        return fact;
    }
}

int main()
{
    int n  = 10;
    long int result = factorial(n);
    printf("Result : %d", result);
}