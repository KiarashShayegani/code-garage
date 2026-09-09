#include <stdio.h>

#define ROWS 2
#define COLS 4

void transpose(int row, int col, int A[row][col], int B[col][row]) {

    for (int i=0; i<row; i++) {
        for (int j=0; j<col; j++) {
            B[j][i] = A[i][j];
        }
    }

}

void matrice_printer(int row, int col, int Arr[row][col]) {

    for (int i=0; i<row; i++) {
        for (int j=0; j<col; j++) {
            printf("%d", Arr[i][j]);
            printf(" ");
        }
        printf("\n");
    }

}

int main()
{
    int row, col, row_after, col_after;
    row = ROWS;
    col = COLS;
    row_after = col;
    col_after = row;
    int A[ROWS][COLS] = {1,2,3,4,5,6,7,8};
    int B[COLS][ROWS];

    printf("Array A (before transpose):\n");
    matrice_printer(row, col, A);

    printf("\n- Transposing matrice..");
    transpose(row, col, A, B);
    printf("\n- Matrice transposed\n");

    printf("\nArray B (after transpose):\n");
    matrice_printer(row_after, col_after, B);

    return 0;

}