from tabulate import tabulate


def create_grid(n):
    assert n % 2 != 0, "Value of n should be odd number"
    return [[0 for _ in range(n)] for _ in range(n)]


def magic_square(arr):
    n = len(arr)

    start_row = 0
    start_col = n // 2

    arr[start_row][start_col] = 1

    for i in range(2, n ** 2 + 1):
        new_row = start_row - 1 if start_row - 1 >= 0 else start_row - 1 + n
        new_col = start_col - 1 if start_col - 1 >= 0 else start_col - 1 + n

        if arr[new_row][new_col] != 0:
            new_row = start_row + 1
            new_col = start_col

        arr[new_row][new_col] = i

        start_row = new_row
        start_col = new_col

    return arr


if __name__ == '__main__':
    grid = create_grid(5)
    magic_grid = magic_square(grid)
    print(tabulate(magic_grid, tablefmt="heavy_grid"))
