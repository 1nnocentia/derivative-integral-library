def function_input(integral=False):
    function = input("Masukkan fungsi f(x) = ")

    # Change ^ to ** if someone typed it in
    function = function.replace('^', '**')

    if integral:
        a = float(input("Masukkan batas bawah (a): "))
        b = float(input("Masukkan batas atas (b): "))
        n = int(input("Masukkan jumlah subinterval (n): "))
        return function, a, b, n
    else:
        x = float(input("Masukkan nilai x: "))
        h_input = input("Masukkan ukuran langkah h (default adalah 1e-5): ")

        # If h not provided
        if not h_input:
            h = 1e-5
        else:
            h = float(h_input)

        return function, x, h
