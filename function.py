def function_input():
    function = input("Masukkan fungsi f(x) = ")
    x = float(input("Masukkan nilai x: "))
    h_input = input("Masukkan ukuran langkah h (default adalah 1e-5): ")

    # Change ^ to ** if someone typed it in
    function = function.replace('^', '**')

    # If h not provided
    if not h_input:
        h = 1e-5
    else:
        h = float(h_input)

    return function, x, h
