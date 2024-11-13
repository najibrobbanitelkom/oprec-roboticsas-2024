def penjumlahan (x,y):
    return x + y
def pengurangan (x,y):
    return x - y
def perkalian (x,y):
    return x * y
def pembagian (x,y):
    if y == 0:
        return "Pembagian tidak terdefinisi"
    return x / y

# main fungsi kalkulator Fizuu
def operasikalkulator():
    while True:
        print ("\nMau Ngapain Nich di Fizu Kalkulator")
        print ("===================================")
        print ("Boleh dipilih yan operasina.....!")
        print ("(satu ajah jangan banyak-banyak😅)")
        print ("1. Penjumlahan")
        print ("2. Pengurangan")
        print ("3. Perkalian")
        print ("4. Pembagian")
        print ("5. untuk keluar dari Fizu kalkulator")
        pilihan = input ("Mau yang mana Nich? (1,2,3,4 atau 5) : ")    
        if pilihan == '5':
            print ("Terimakasih Sudah Memilih Fizu Kalkulator.")
            break 
        elif pilihan not in ('1','2','3','4'):
            print ("maaf ya, angka yang kamu masukkan tidak ada dalam daftar")
            continue
        try: 
            angk1 = float (input("Masukkan angka Pertama : "))
            angk2 = float (input("Masukkan angka ke-dua : "))
        except ValueError:
            print("Yang kamu masukkan bukan angka loh, ayo coba lagi masukkan angka Ya!")
            continue
        if pilihan == '1':
            print(f"Hasil Penjumlahan dari : {angk1} + {angk2} = {penjumlahan(angk1,angk2)}")
        elif pilihan == '2':
            print(f"Hasil Pengurangan dari: {angk1} - {angk2} = {pengurangan(angk1,angk2)}")
        elif pilihan == '3':
            print(f"Hasil Perkalian dari: {angk1} * {angk2} = {perkalian(angk1,angk2)}")
        elif pilihan == '4':
            print(f"Hasil pembagian dari : {angk1} / {angk2} = {pembagian(angk1,angk2)}")

operasikalkulator()