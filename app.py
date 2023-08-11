def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid!")
        return

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = tambah(angka1, angka2)
        operator = "+"
    elif pilihan == '2':
        hasil = kurang(angka1, angka2)
        operator = "-"
    elif pilihan == '3':
        hasil = kali(angka1, angka2)
        operator = "*"
    else:
        hasil = bagi(angka1, angka2)
        operator = "/"

    print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")

if __name__ == "__main__":
    kalkulator()