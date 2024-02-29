# Напишите функцию для транспонирования матрицы
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Пример использования
matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)