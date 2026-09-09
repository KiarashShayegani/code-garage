#include <stdio.h>

#define ROWS 3
#define COLS 4
#define MIDS 2

void matrice_mult(int row, int col, int mid,
                int A[row][mid],
                int B[mid][col],
                int C[row][col]) {

    for (int i=0; i<row; i++) {
        for (int j=0; j<col; j++) {
            C[i][j] = 0;
            for (int k=0; k<mid; k++) {

                C[i][j] += A[i][k] * B[k][j];
            }
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

    int row, col, mid;
    row = ROWS;
    col = COLS;
    mid = MIDS;
    int A[ROWS][MIDS] = {1,2,3,4,5,6};
    int B[MIDS][COLS] = {5,-2,2,1,8,3,4,10};
    int C[ROWS][COLS];

    printf("Matrice A:\n");
    matrice_printer(row, mid, A);

    printf("\nMatrice B:\n");
    matrice_printer(mid, col, B);

    printf("\nMultiplying matrices..");
    matrice_mult(row, col, mid, A, B, C);
    printf("\nMultiplication completed!");

    printf("\n\nMatrice C:\n");
    matrice_printer(row, col, C);

    return 0;
}