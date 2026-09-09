#include <stdio.h>

int fibo_simple(int n) {
    
    int n1=0, n2=1, sum;
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        for (int i=2; i<=n; i++) {

            sum = n1 + n2;
            n1 = n2;
            n2 = sum;
        }
        return sum;
    }
}

int fibo_recur(int n) {
    
    int sum;
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else {
        sum = fibo_recur(n - 1) + fibo_recur(n - 2);
    }
    return sum;
}

int main() {

    int number = 8;
    int result = fibo_simple(number);
    printf("Result (fibo simple): %d", result);
    result = fibo_recur(number);
    printf("\nResult (fibo recursive): %d", result);

}