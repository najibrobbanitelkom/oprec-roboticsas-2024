import math

def menu():
      print("[Angka!]:\n"
            "1. Tambah\n"
            "2. Kurang\n"
            "3. Kali\n"
            "4. Bagi\n"
            "5. Mod\n"
            "6. Pangkat\n"
            "7.Akar")

while True:
      
      X = int(input("Masukkan Nilai x: "))
      menu()
      operator = int(input("pilihlah angkanya mau diapakan? "))

      if operator != 7:
            Y = int(input("Masukkan Nilai Y: "))

      if operator == 1:
            print(f"Hasilnya [X] + [Y] adalah = {X + Y}")
      elif operator == 2:
            print(f"Hasilnya [X] - [Y] adalah = {X - Y}")
      elif operator == 3:
            print(f"Hasilnya [X] * [Y] adalah = {X * Y}")
      elif operator == 4:
            if Y != 0:
                  print(f"Hasilnya [X] / [Y] adalah = {X / Y}")
            else:
                  print("Error: Nilai Tidak Terdefinisi!")
      elif operator == 5:
            print(f"Hasilnya [X] % [Y] adalah = {X % Y}")
      elif operator == 6:
            print(f"Hasilnya [X] ** [Y] adalah = {X ** Y}")
      elif operator == 7:
            if X >= 0:
                  print(f"Hasil akar dari [X] adalah = {math.sqrt(X)}")
            else:
                  print("Error: Tidak bisa menghitung akar dari bilangan negatif.")
      else:
            print("Maaf, Tidak ada pilihan tersebut")