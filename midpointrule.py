import math

def midpoint_rule_n(f, a, b, n):
    """
    Menghitung pendekatan integral tentu menggunakan metode Midpoint Rule dengan n subinterval.

    Langkah-langkah:
    1. Hitung panjang tiap subinterval: h = (b - a) / n
    2. Untuk setiap subinterval ke-i:
        a. Hitung batas bawah subinterval ke-i: xi = a + i * h
        b. Hitung titik tengah: midpoint = xi + h / 2
        c. Hitung nilai fungsi pada titik tengah: f(midpoint)
        d. Tambahkan hasil f(midpoint) ke total penjumlahan
    3. Kalikan total penjumlahan dengan h untuk mendapatkan nilai pendekatan integral

    Parameter:
    f -- fungsi Python yang ingin diintegrasikan (contoh: lambda x: x**2)
    a -- batas bawah integrasi
    b -- batas atas integrasi
    n -- jumlah subinterval (semakin besar, semakin akurat)

    Return:
    float -- Nilai pendekatan integral tentu dari fungsi f di interval [a, b]

    Contoh:
    >>> midpoint_rule_n(lambda x: x**2, 0, 2, 4)
    2.625
    """
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + i * h
        midpoint = xi + h / 2
        total += f(midpoint)
    return h * total


# Program Interaktif
print("=== Midpoint Rule Calculator ===")
print("Gunakan fungsi Python yang valid, contoh: x**2, math.sin(x), 1/x, math.exp(x), dll.\n")

# Input dari pengguna
fungsi_input = input("Masukkan fungsi f(x): ")
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
n = int(input("Masukkan jumlah subinterval (n): "))

# Buat fungsi dari input string
def f(x):
    return eval(fungsi_input)

# Hitung dan tampilkan hasil
hasil = midpoint_rule_n(f, a, b, n)
print(f"\nHasil pendekatan integral dari f(x) = {fungsi_input} pada interval [{a}, {b}] dengan {n} subinterval:")
print(f"≈ {hasil}")
