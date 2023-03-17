# Sebelum menjalankan program, pastikan Anda telah menginstal numpy dengan menjalankan perintah "pip install numpy" di terminal atau command prompt
import numpy as np

# Inisialisasi matriks A
A = np.array([[1, 2], [3, 4], [5, 6]])

# Transposisi matriks A
A_transpose = np.transpose(A)

# Cetak matriks A dan hasil transposisinya
print("Matriks A:")
print(A)
print("\nHasil transposisi matriks A:")
print(A_transpose)
