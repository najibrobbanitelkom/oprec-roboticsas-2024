def filter_even_numbers(angka):
    angkaGenap = []
    for number in angka:
        if number % 2 == 0:
            angkaGenap.append(number)
    return angkaGenap


angka = []

jumlah_input = int(input("Masukkan jumlah angka yang ingin di input: "))

for i in range(jumlah_input):
    angka_input = int(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(angka_input)

hasil = filter_even_numbers(angka)
print("List angka genap:", hasil)