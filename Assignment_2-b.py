import threading


def compute_dot_product(row, col, result, row_idx):
    result[row_idx] = sum(x * y for x, y in zip(row, col))


def compute_vector_parallel(matrix_a, matrix_b):
    n = len(matrix_a)
    m = len(matrix_b[0])
    c = [0] * n
    threads = []

    for i in range(n):
        row = matrix_a[i]
        col = [matrix_b[j][i] for j in range(m)]
        thread = threading.Thread(target=compute_dot_product, args=(row, col, c, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return c


# Example usage:
matrix_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_b = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

result = compute_vector_parallel(matrix_a, matrix_b)
print(result)
