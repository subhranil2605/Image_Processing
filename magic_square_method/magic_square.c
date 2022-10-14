#include <stdio.h>
#include <stdlib.h>

// creates a 2D square array of 0s with given number of rows
int **createGrid(int n) {
    int i, j;

    // 2D array of ints
    int **matrix;

    matrix = malloc(sizeof(int *) * n);

    for (i = 0; i < n; i++) {
        matrix[i] = malloc(sizeof(int) * n);
    }

    // fill the matrix with 0s
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            matrix[i][j] = 0;
        }
    }

    return matrix;
}

// creates a magic square array of given n
int **magicSquare(int **arr, int num) {
    int i, j;
    int startRow, startCol;

    startRow = 0;
    startCol = num / 2;

    arr[startRow][startCol] = 1;    // adding the 1

    for (i = 2; i < num * num + 1; i++) {
        int newRow = startRow - 1;  // one step up
        int newCol = startCol - 1;  // one step left

        // if the row number becomes negative then make it last row
        if (newRow < 0) {
            newRow += num;  
        }

        // if the column number becomes negative then make it last column
        if (newCol < 0) {
            newCol += num;
        }

        // if the cell is equipped already
        if (arr[newRow][newCol] != 0) {
            newRow = startRow + 1;  // one step down
            newCol = startCol;  // same column
        }

        // filling the array
        arr[newRow][newCol] = i;

        // updating startRow, startCol variables
        startRow = newRow;
        startCol = newCol;
    }

    return arr;
}

// prints the 2D array
void printArray(int **arr, int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }
}

void main() {
    int n;
    int i, j;
    int **arr;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    // check if the n's value even
    if (n % 2 == 0) {
        printf("n's value should not be even!!!\n");
        return;
    }

    arr = createGrid(n);    // creating a 2D array of 0s
    arr = magicSquare(arr, n);  // magic square 

    printf("The magic-square for n = %d is:\n", n);
    printArray(arr, n);

    // free the memory
    for (i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);
}