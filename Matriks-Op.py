# Sebelum menjalankan program, pastikan Anda telah menginstal numpy dengan menjalankan perintah "pip install numpy" di terminal atau command prompt
import numpy as np

# Inisialisasi matriks A dan B
A = np.array([[2, -4], [1, 3]])
B = np.array([[12, -8], [-11, 29]])

# Penjumlahan matriks A dan B
C = A + B
print("Penjumlahan matriks A dan B:")
print(C)

# Pengurangan matriks A dan B
C = A - B
print("Pengurangan matriks A dan B:")
print(C)

# Perkalian matriks A dan B
C = np.dot(A, B)
print("Perkalian matriks A dan B:")
print(C)
