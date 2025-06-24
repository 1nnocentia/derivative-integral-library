import math


def central_difference_basic(f,x,h):
    """
    Menghitung aproksimasi turunan pertama dari sebuah fungsi di titik x
    menggunakan metode selisih tengah (central difference).

    Parameters
    ----------
    f : Fungsi yang akan diturunkan. Harus menerima satu argumen numerik (float atau int)
        dan mengembalikan nilai numerik.
    x : Titik di mana turunan akan dihitung.
    h : Ukuran langkah kecil (step size). Nilai yang sangat kecil akan memberikan
        aproksimasi yang lebih baik, tetapi terlalu kecil dapat menyebabkan
        error numerik. Default-nya adalah 1e-5.

    Returns
    -------
    float
        Nilai aproksimasi dari turunan pertama fungsi f di titik x.
    """
    if not callable(f):
        raise TypeError("Parameter 'f' harus berupa fungsi yang bisa dipanggil.")

    return (f(x + h) - f(x - h)) / (2 * h)