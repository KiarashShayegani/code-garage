// Linear search program

#include <stdio.h>

int main()
{
    int myArr[] = {1,5,8,65,7,6,24,78,3,9,243};
    int length = sizeof(myArr) / sizeof(myArr[0]);

    int choice;
    printf("What number to look for: ");
    scanf("%d", &choice);

    for (int i=0; i < length; i++) {
        if (myArr[i] == choice) {
            printf("Found number %d at %d", choice, i);
        }
    }

    return 0;
}