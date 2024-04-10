def dot_product_vector_serial(A, B):
    n = len(A)
    C = [0] * n
    for i in range(n):
        for j in range(n):
            C[i] += A[i][j] * B[j][i]
    return C


# Example usage
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

result = dot_product_vector_serial(A, B)
print(result)
