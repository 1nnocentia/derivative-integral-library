import math
from forward_difference import forward_difference_first_order

def menu():
    print("-- Metode Numerikal Turunan dan Integral --")
    print("Pilih Metode:")
    print("1. Turunan")
    print("2. Integral")
    choice = input("Masukkan pilihan (1/2): ")
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
                    print("Central Difference belum diimplementasikan.")
                case "3":
                    print("Backward Difference belum diimplementasikan.")
                case _:
                    print("Pilihan tidak valid.")

if __main__ == "__main__":
    menu()