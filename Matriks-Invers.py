# Sebelum menjalankan program, pastikan Anda telah menginstal numpy dengan menjalankan perintah "pip install numpy" di terminal atau command prompt
import numpy as np

# Inisialisasi matriks A
A = np.array([[1, 2], [3, 4]])

# Menghitung invers matriks A
A_inv = np.linalg.inv(A)

# Cetak matriks A dan invers matriks A
print("Matriks A:")
print(A)
print("\nInvers matriks A:")
print(A_inv)
