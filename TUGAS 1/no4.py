def filter_event_numbers(numbers):
    jumlahAngka = []

    for angka in numbers:
        if angka % 2 == 0:
           jumlahAngka.append(angka)
    
    print(jumlahAngka)

numbers = list(map(int, input("Masukkan bilanga yang kamu mau sobat  : ").split()))
filter_event_numbers(numbers)