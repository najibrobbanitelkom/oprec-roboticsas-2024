def filter_even_numbers(angka):
    Genap = []
    for number in angka:
        if number % 2 == 0:
            Genap.append(number)
    return Genap


angka = []

jumlah = int(input("Masukkan jumlah angka yang ingin di input: "))

for i in range(jumlah):
    input_angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(input_angka)

result = filter_even_numbers(angka)
print("List angka genap:", result)