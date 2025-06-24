# Metode Numerik untuk Turunan dan Integral 📊

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat&logo=github-actions&logoColor=white)](#)

---

## 📦 Deskripsi

Repositori ini berisi implementasi **metode numerik** untuk menghitung:
- Turunan pertama (Forward, Backward, Central Difference)
- Integral tentu (Trapezoidal dan Simpson’s 1/3 Rule)

Library ini mendukung input fungsi interaktif melalui `main.py` dan dilengkapi dokumentasi serta studi kasus untuk keperluan edukatif.

---

## 📁 Struktur File

- `forward_difference.py` - Metode selisih maju (Forward Difference)
- `backward_difference.py` - Metode selisih mundur (Backward Difference)
- `central_difference.py` - Metode selisih tengah (Central Difference)
- `trapezoidal_n_order.py` - Aturan trapesium untuk integral
- `simpson.py` - Aturan Simpson 1/3 untuk integral
- `midpointrule.py` - Menghitung integral dengan metode Midpoint Rule (dengan `n` subinterval)
- `function.py` - Utility fungsi input string menjadi fungsi
- `main.py` - Program interaktif
- `README.md` - Dokumentasi

---

## 🧪 Studi Kasus

### 📌 Kasus A – Titik Ekstrim Lokal

**Fungsi:**  
\[
f(x) = x^3 - 3x^2 + 2
\]

**Langkah:**
1. Hitung turunan numerik \( f'(x) \) menggunakan Central Difference.
2. Perkirakan titik stasioner (di mana \( f'(x) \approx 0 \)) pada interval \([0, 3]\).
3. Bandingkan hasilnya dengan titik ekstrem dari turunan eksak \( f'(x) = 3x^2 - 6x \).

**Kode:**
```python
from central_difference import central_difference_basic

def f(x): return x**3 - 3*x**2 + 2
def df(x): return central_difference_basic(f, x, 1e-5)

# Estimasi turunan pada titik-titik
for x in [0, 1, 2, 3]:
    print(f"f'({x}) ≈ {df(x):.5f}")
```

**Hasil Eksak:**
\[
f'(x) = 3x(x - 2) \Rightarrow x = 0 \text{ dan } x = 2
\]

---

### 📌 Kasus B – Integral Tentu

**Fungsi:**  
\[
f(x) = x^2,\quad \text{dengan interval } [0, 1]
\]

**Langkah:**
1. Hitung integral menggunakan metode:
   - Trapezoidal (`n=100`)
   - Simpson 1/3 (`n=100`)
2. Bandingkan dengan hasil analitik:
   \[
   \int_0^1 x^2 dx = \frac{1}{3} \approx 0.3333
   \]

**Kode:**
```python
from trapezoidal_n_order import trapezoidal_n_order
from simpson import simpsons_one_third_rule

def f(x): return x**2
a, b, n = 0, 1, 100

hasil_trap = trapezoidal_n_order(f, a, b, n)
hasil_simp = simpsons_one_third_rule(f, a, b, n)

print(f"Trapezoidal ≈ {hasil_trap:.10f}")
print(f"Simpson 1/3 ≈ {hasil_simp:.10f}")
print(f"Solusi eksak  ≈ {1/3:.10f}")
```

---

## 🏁 Menjalankan Program

Jalankan:
```bash
python main.py
```

Ikuti menu untuk memilih metode turunan/integral yang ingin digunakan.

---

## 🛠 Persyaratan

- Python 3.8+
- Tidak memerlukan library eksternal

---

## 📚 Catatan

- Gunakan `math.` jika ingin menggunakan fungsi seperti `sin`, `cos`, `exp`, dll.
- Selalu pastikan `n` adalah **bilangan genap** untuk Simpson 1/3 Rule.
- `eval()` digunakan untuk evaluasi fungsi dengan hati-hati (tidak aman untuk input dari user tidak terpercaya).

---


### ➕ Metode Tambahan – Midpoint Rule

**Fungsi:**  
\[
f(x) = x^2,\quad \text{dengan interval } [0, 1]
\]

**Deskripsi:**
Midpoint Rule menghitung integral dengan menggunakan nilai fungsi pada titik tengah setiap subinterval.

**Kode:**
```python
from midpointrule import midpoint_rule_n

def f(x): return x**2
a, b, n = 0, 1, 100

hasil_mid = midpoint_rule_n(f, a, b, n)
print(f"Midpoint Rule ≈ {hasil_mid:.10f}")
```

**Bandingkan dengan hasil eksak:**
\[
\int_0^1 x^2 dx = \frac{1}{3} \approx 0.3333
\]

Midpoint Rule cocok digunakan sebagai alternatif sederhana dan cepat untuk integral numerik, terutama bila fungsi relatif halus.
