# def multiply_matrices(A, B, C, low_row_a, high_row_a, low_col_a, high_col_a, low_row_b, high_row_b, low_col_b, high_col_b):
#
#   # Base Case
#   if high_row_a - low_row_a == 1 and high_col_a - low_col_a == 1 and high_row_b - low_row_b == 1 and high_col_b - low_col_b == 1:
#     C[low_row_a][low_col_b] = A[low_row_a][low_col_a] * B[low_row_b][low_col_b]
#     return
#
#   # Divide
#   mid_row_a = (low_row_a + high_row_a) // 2
#   mid_col_a = (low_col_a + high_col_a) // 2
#   mid_row_b = (low_row_b + high_col_b) // 2
#   mid_col_b = (low_col_b + high_col_b) // 2
#
#   # Spawn Threads
#   thread1 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, low_col_a, mid_col_a, low_row_b, mid_row_b, low_col_b, mid_col_b
#   thread2 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, mid_col_a, high_col_a, low_row_b, mid_row_b, low_col_b, mid_col_b
#   thread3 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, low_col_a, mid_col_a, mid_row_b, high_row_b, mid_col_b, high_col_b
#   thread4 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, mid_col_a, high_col_a, mid_row_b, high_row_b, mid_col_b, high_col_b
#   thread5 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, low_col_a, mid_col_a, mid_row_b, mid_row_b, mid_col_b, high_col_b
#   thread6 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, mid_col_a, high_col_a, mid_row_b, high_row_b, mid_col_b, high_col_b
#   thread7 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, low_col_a, mid_col_a, mid_row_b, mid_row_b, low_col_b, high_col_b
#   thread8 = spawn multiply_matrices, A, B, C, low_row_a, mid_row_a, mid_col_a, high_col_a, mid_row_b, high_row_b, mid_col_b, high_col_b
#
#   # Sync (wait for all threads to finish)
#   sync thread1, thread2, thread3, thread4, thread5, thread6, thread7, thread8
#
#   # Combine
#   for i in range(low_row_a, high_row_a):
#     for j in range(low_col_b, high_col_b):
#       for k in range(low_col_a, high_col_a):
#         C[i][j] += C[i][k] * B[k][j]
#
#   return C
