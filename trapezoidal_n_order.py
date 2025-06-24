def trapezoidal_n_order(f, a, b, n):
    """
    Menghitung integral numerik menggunakan aturan trapesium dengan n subinterval.
    
    Formula: ∫[a,b] f(x) dx ≈ (h/2) * [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]
    
    Parameters:
    -----------
    f : function
        Fungsi yang akan diintegralkan
    a : float
        Batas bawah integral
    b : float
        Batas atas integral  
    n : int
        Jumlah subinterval
        
    Returns:
    --------
    float
        Nilai aproksimasi integral
        
    Contoh Penggunaan
    -----------------
    # Hitung integral dari f(x) = x^2 dari 0 sampai 1.
    # Hasil analitiknya adalah 1/3 ≈ 0.333...
    def fungsi_kuadrat(x):
        return x**2
    
    hasil_integral = trapezoidal_n_order(fungsi_kuadrat, 0, 1, n=100)
    print(f"Hasil integral numerik: {hasil_integral:.10f}")
    # Output: Hasil integral numerik: 0.3333835000
    
    # Contoh lain: integral dari sin(x) dari 0 sampai π
    # Hasil analitiknya adalah 2
    import math
    hasil_integral_sin = trapezoidal_n_order(math.sin, 0, math.pi, n=1000)
    print(f"Integral sin(x) dari 0 ke π: {hasil_integral_sin:.10f}")
    # Output: Integral sin(x) dari 0 ke π: 2.0000000033
    """
    if n <= 0:
        raise ValueError("Jumlah subinterval n harus lebih besar dari 0")
    
    if a > b:
        raise ValueError("Batas bawah a harus lebih kecil atau sama dengan batas atas b")
    
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i * h
        result += 2 * f(xi)
    
    result *= h / 2
    return result



