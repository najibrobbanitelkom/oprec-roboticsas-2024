#kalkulator menghitung umur
from datetime import datetime

def hitung_umur(tanggal_lahir):
    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    hari_ini = datetime.today()
    umur = hari_ini.year - tanggal_lahir.year
    if (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day):
        umur -= 1
    return umur

tanggal_lahir = input("Masukkan tanggal lahir Anda (format: YYYY-MM-DD): ")
umur = hitung_umur(tanggal_lahir)
print(f"Umur Anda adalah: {umur} tahun")