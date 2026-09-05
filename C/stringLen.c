// Writing strlen function from scratch

#include <stdio.h>
#include <stdlib.h>

int stringLen(char *string) {

    int counter;
    for (int ch = 0; string[ch] != '\0'; ch++) {
        counter++;
    }

    return counter;
}


int main() {
    
    int length;
    char *str = "Hello!";
    length = stringLen(str);

    printf("Length of string is = %d", length);

    return 0;
}

