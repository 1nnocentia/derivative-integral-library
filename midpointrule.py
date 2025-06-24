import math

def midpoint_rule_n(f, a, b, n):
    """
    Midpoint Rule untuk n subinterval.

    Parameter:
    f -- fungsi yang ingin diintegrasikan
    a -- batas bawah
    b -- batas atas
    n -- jumlah subinterval

    Return:
    Nilai pendekatan integral
    """
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + i * h
        midpoint = xi + h / 2
        total += f(midpoint)
    return h * total


# Input dari pengguna
print("Menghitung integral tentu dengan Midpoint Rule")
print("Gunakan fungsi yang dapat dievaluasi dengan math, misal: sin(x), x**2, log(x), dll.")

fungsi_input = input("Masukkan fungsi f(x): ")  # contoh: x**2 atau math.sin(x)
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
n = int(input("Masukkan jumlah subinterval (n): "))

# Buat fungsi dari input string
def f(x):
    return eval(fungsi_input)

# Hitung hasil
hasil = midpoint_rule_n(f, a, b, n)
print(f"Hasil integral dari {fungsi_input} antara {a} sampai {b} dengan {n} subinterval adalah: {hasil}")
