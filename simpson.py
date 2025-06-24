def simpsons_one_third_rule(f, a, b, n=100):
    """
    Menghitung aproksimasi integral tentu dari sebuah fungsi dari a ke b
    menggunakan kaidah Simpson 1/3.

    Formula: ∫[a,b] f(x) dx ≈ (h/3) * [f(x₀) + 4f(x₁) + 2f(x₂) + ... + 4f(xₙ₋₁) + f(xₙ)]

    Parameters
    ----------
    f : function
        Fungsi yang akan diintegralkan.
    a : float atau int
        Batas bawah integrasi.
    b : float atau int
        Batas atas integrasi.
    n : int, opsional
        Jumlah sub-interval. HARUS berupa bilangan genap dan positif.
        Semakin besar n, semakin akurat hasilnya. Default-nya 100.

    Returns
    -------
    float
        Nilai aproksimasi dari integral f(x) dari a sampai b.

    Contoh Penggunaan
    -----------------
    # Hitung integral dari f(x) = x^2 dari 0 sampai 1.
    # Hasil analitiknya adalah 1/3 ≈ 0.333...
        def fungsi_kuadrat(x):
        return x**2
    ...
    hasil_integral = simpsons_one_third_rule(fungsi_kuadrat, 0, 1, n=100)
    print(f"Hasil integral numerik: {hasil_integral:.10f}")
    Hasil integral numerik: 0.3333333333
    """
    if not callable(f):
        raise TypeError("Parameter 'f' harus berupa fungsi yang bisa dipanggil.")
    if n % 2 != 0 or n <= 0:
        raise ValueError("Jumlah interval 'n' harus berupa bilangan genap positif.")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    
    for i in range(2, n, 2):
        integral += 2 * f(a + i * h)
        
    integral *= h / 3
    return integral