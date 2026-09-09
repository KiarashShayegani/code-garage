#include <stdio.h>

void hanoi(int n, char a, char b, char c, int *counter) {

    if (n == 1) {
        printf("%c --> %c\n", a, c);
        (*counter)++;
    } else {
        hanoi(n-1, a, c ,b, counter);
        printf("%c --> %c\n", a, c);
        (*counter)++;
        hanoi(n-1, b, a, c, counter);
    }

}

int main() {
    int n = 3, counter=0;
    char a = 'A', b = 'B', c = 'C';
    printf("Running hanoi(n=%d):\n", n);
    hanoi(n, a, b, c, &counter);
    printf("\nNumber of moves: %d", counter);

    return 0;
}