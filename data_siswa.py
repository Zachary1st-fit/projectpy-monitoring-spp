def menu_siswa(siswa):
    while True:
        print()
        print("==============================")
        print("         DATA SISWA")
        print("==============================")
        print("1. Tambah Siswa")
        print("2. Lihat Semua Siswa")
        print("3. Hapus Siswa")
        print("4. Kembali")

        pilihan = input("Pilih menu siswa: ")

        if pilihan == "1":
            tambah_siswa(siswa)
        elif pilihan == "2":
            lihat_siswa(siswa)
        elif pilihan == "3":
            hapus_siswa(siswa)
        elif pilihan == "4":
            print("\nKembali ke menu utama.")
            break
        else:
            print("\nMenu siswa tidak tersedia!")


def tambah_siswa(siswa):
    print("\n>>> TAMBAH SISWA <<<")
    nisn = input("Masukkan NISN: ")

    for data in siswa:
        if data["nisn"] == nisn:
            print("NISN sudah terdaftar!")
            return

    nama = input("Masukkan nama: ")
    kelas = input("Masukkan kelas: ")
    siswa.append({"nisn": nisn, "nama": nama, "kelas": kelas})
    print("\nData siswa berhasil ditambahkan!")


def lihat_siswa(siswa):
    print("\n>>> LIHAT SEMUA SISWA <<<")
    if len(siswa) == 0:
        print("Belum ada data siswa.")
        return

    for data in siswa:
        print("------------------------------")
        print("NISN  :", data["nisn"])
        print("Nama  :", data["nama"])
        print("Kelas :", data["kelas"])
    print("------------------------------")


def hapus_siswa(siswa):
    print("\n>>> HAPUS SISWA <<<")
    nisn_hapus = input("Masukkan NISN yang ingin dihapus: ")

    for data in siswa:
        if data["nisn"] == nisn_hapus:
            siswa.remove(data)
            print("Data siswa berhasil dihapus!")
            return

    print("NISN tidak ditemukan!")