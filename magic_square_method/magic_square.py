from tabulate import tabulate
import time


list_of_list_of_int = list[list[int, ...], ...]

def create_grid(n: int = 3) -> list_of_list_of_int:
    """
    Creates a 2D list of 0s
    """

    assert n % 2 != 0, "n should not be an even number!!!"
    
    grid: list_of_list_of_int = [[0 for _ in range(n)] for _ in range(n)]
    return grid


def magic_square(arr: list_of_list_of_int) -> list_of_list_of_int:
    """
    Fill the grid using magic-square method
    """

    # size of the array
    n: int = len(arr)

    # for starting with 1 at the middle column and first row
    start_row: int = 0
    start_col: int = n // 2

    # starting with 1
    arr[start_row][start_col] = 1

    # fill up the others
    for i in range(2, n ** 2 + 1):
        new_row: int = start_row - 1 # move one up
        new_col: int = start_col - 1 # move one left

        if arr[new_row][new_col] == 0:
            if new_row < 0: # if new row becomes negative
                new_row = n + new_row # new row becomes the last row

            if new_col < 0: # if new column becomes negative
                new_col = n + new_col # new column becomes the last column
        else:
            new_row = start_row + 1 # move one down
            new_col = start_col # same column

        # updating the array values 
        arr[new_row][new_col] = i

        # updating start_row and start_column
        start_row = new_row
        start_col = new_col

    return arr
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    
    n: int = 5
    arr: list_of_list_of_int = create_grid(n)
    arr: list_of_list_of_int = magic_square(arr)
    
    print(f"Execution Time: {(time.perf_counter() - start_time)} seconds\n")
    print(f"The magic-square table for {n = } is: ")
    print(tabulate(arr, tablefmt="grid"))
