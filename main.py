from data_siswa import menu_siswa
from pembayaran import menu_pembayaran
from statistik import tampilkan_statistik

siswa = []
pembayaran = []

while True:
    print()
    print("==============================")
    print("    SISTEM MANAJEMEN SPP")
    print("==============================")
    print("1. Data Siswa")
    print("2. Pembayaran SPP")
    print("3. Statistik")
    print("4. Keluar")

    pilihan = input("Pilih menu utama: ")

    if pilihan == "1":
        menu_siswa(siswa)
    elif pilihan == "2":
        menu_pembayaran(siswa, pembayaran)
    elif pilihan == "3":
        tampilkan_statistik(siswa, pembayaran)
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Menu tidak tersedia!")