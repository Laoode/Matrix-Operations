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

def transpose(matrix):
    n = len(matrix)
    transposed = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed

def cofactor(matrix):
    n = len(matrix)
    cofactored = []
    for i in range(n):
        row = []
        for j in range(n):
            sign = (-1) ** (i+j)
            sub_matrix = []
            for k in range(n):
                if k != i:
                    sub_row = []
                    for l in range(n):
                        if l != j:
                            sub_row.append(matrix[k][l])
                    sub_matrix.append(sub_row)
            sub_det = det(sub_matrix)
            row.append(sign * sub_det)
        cofactored.append(row)
    return cofactored

def inverse(matrix):
    determinant = det(matrix)
    if determinant == 0:
        print("Matriks tidak memiliki invers.")
        return None
    else:
        n = len(matrix)
        cofactors = cofactor(matrix)
        adjugate = transpose(cofactors)
        inverted = []
        for i in range(n):
            row = []
            for j in range(n):
                element = adjugate[i][j] / determinant
                row.append(round(element, 2))
            inverted.append(row)
        return inverted

matrix = input_matrix()
if matrix is not None:
    print("Matriks yang dicari inversnya:")
    for row in matrix:
        print(row)
    inverse_matrix = inverse(matrix)
    if inverse_matrix:
        print("Invers matriks:")
        for row in inverse_matrix:
            print(row)
