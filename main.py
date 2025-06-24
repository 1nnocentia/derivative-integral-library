import math
from central_difference import central_difference_basic
from forward_difference import forward_difference_first_order
from trapezoidal_n_order import trapezoidal_n_order

from function import function_input

def menu():
    while True:
        print("""
===== Metode Numerikal Turunan dan Integral =====
1. Turunan
2. Integral
3. Exit
=================================================""")
        choice = input("Mau pilih metode yang mana? (1/2/3): ")
        if choice not in ["1", "2", "3"]:
            print("Pilihan tidak valid. Silakan coba lagi.")
        match choice:
            case "1": 
                print("Metode Turunan Apa yang ingin Anda gunakan?")
                print("1. Forward Difference")
                print("2. Central Difference")
                print("3. Backward Difference")
                sub_choice = input("Masukkan pilihan (1/2/3): ")
                match sub_choice:
                    case "1":
                        print("Kamu memilih forward difference.")
                        print("1. First Order")
                        print("2. Second Order")
                        imp_choice = print("Yang mana ingin kamu gunakan(1/2): ")
                    case "2":
                        print("Kamu memilih central difference.")
                        function, x, h = function_input()

                        def f(x):
                            return eval(function, {"x": x, "math": math})

                        print("Hasil: ", central_difference_basic(f, x, h))

                    case "3":
                        print("Backward Difference belum diimplementasikan.")
                    case _:
                        print("Pilihan tidak valid.")
            case "2":
                print("Metode Integral Apa yang ingin Anda gunakan?")
                print("1. Trapezoidal Rule")
                print("2. Simpson's Rule")
                sub_choice = input("Masukkan pilihan (1/2): ")
                match sub_choice:
                    case "1":
                        print("Kamu memilih Trapezoidal Rule.")
                        function, a, b, n = function_input(integral=True)

                        def f(x):
                            return eval(function, {"x": x, "math": math})
                        
                        hasil = trapezoidal_n_order(f, a, b, n)
                        print(f"Hasil integral numerik: {hasil}")
                    case "2":
                        print("Simpson's Rule belum diimplementasikan.")
                    case _:
                        print("Pilihan tidak valid.")
            case "3":
                print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
                break

if __name__ == "__main__":
    menu()