def trapezoidal_n_order(f, a, b, n):
    """
    Menghitung integral numerik menggunakan aturan trapesium dengan n subinterval.
    
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



