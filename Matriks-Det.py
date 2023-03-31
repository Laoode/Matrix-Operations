# Fungsi untuk meminta input matriks
def input_matrix():
    n = int(input("Masukkan ukuran matriks: "))
    if n > 6:
        print("Maaf, ukuran matriks terlalu besar (maksimal 6x6).")
        return None
    else:
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                value = float(input("Masukkan nilai pada baris {} kolom {}: ".format(i+1, j+1)))
                row.append(value)
            matrix.append(row)
        return matrix

# Fungsi untuk mencetak matriks
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Fungsi untuk menghitung determinan matriks
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        result = 0
        for j in range(n):
            sign = (-1) ** j
            sub_matrix = []
            for i in range(1, n):
                row = []
                for k in range(n):
                    if k != j:
                        row.append(matrix[i][k])
                sub_matrix.append(row)
            sub_det = det(sub_matrix)
            result += sign * matrix[0][j] * sub_det
        return result

# Meminta input matriks dari pengguna
matrix = input_matrix()
if matrix is not None:
    print("Matriks yang dihitung determinannya:")
    print_matrix(matrix)
    print("Determinan:", det(matrix))
