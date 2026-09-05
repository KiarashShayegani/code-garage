#include <stdio.h>

int main() {

    unsigned int grade;
    printf("Etner your grade: ");
    scanf("%d", &grade);

    if (grade > 100){
        printf("\nGrades can not be above 100!");
    } else if (grade>=90 && grade<=100) {
        printf("\ngrade is A");
    } else if (grade>=80 && grade<90) {
        printf("\ngrade is B");
    } else if (grade>=70 && grade<80) {
        printf("\ngrade is C");
    } else if (grade>=60 && grade<70) {
        printf("\ngrade is D");
    } else {
        printf("\ngrade is F");
    }

    return 0;
};



