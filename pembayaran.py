NOMINAL_SPP = 150000

BULAN = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]


def menu_pembayaran(siswa, pembayaran):
    while True:
        print()
        print("==============================")
        print("      PEMBAYARAN SPP")
        print("==============================")
        print("1. Bayar SPP")
        print("2. Kembali")

        pilihan = input("Pilih menu pembayaran: ")

        if pilihan == "1":
            bayar_spp(siswa, pembayaran)
        elif pilihan == "2":
            print("\nKembali ke menu utama.")
            break
        else:
            print("\nMenu pembayaran tidak tersedia!")


def bayar_spp(siswa, pembayaran):
    print("\n>>> BAYAR SPP <<<")

    if len(siswa) == 0:
        print("Belum ada data siswa.")
        print("Silakan tambahkan siswa terlebih dahulu.")
        return

    nisn_bayar = input("Masukkan NISN siswa: ")

    siswa_ditemukan = None
    for data in siswa:
        if data["nisn"] == nisn_bayar:
            siswa_ditemukan = data
            break

    if siswa_ditemukan is None:
        print("\nNISN tidak ditemukan!")
        return

    print()
    print("==============================")
    print("       DATA SISWA")
    print("==============================")
    print("NISN  :", siswa_ditemukan["nisn"])
    print("Nama  :", siswa_ditemukan["nama"])
    print("Kelas :", siswa_ditemukan["kelas"])

    print()
    print("==============================")
    print("      PILIH BULAN SPP")
    print("==============================")
    for i in range(len(BULAN)):
        print(i + 1, ".", BULAN[i])

    pilihan_bulan = input("Pilih bulan: ")

    if not pilihan_bulan.isdigit():
        print("\nMasukkan nomor bulan!")
        return

    nomor_bulan = int(pilihan_bulan)
    if nomor_bulan < 1 or nomor_bulan > len(BULAN):
        print("\nNomor bulan tidak tersedia!")
        return

    bulan_dipilih = BULAN[nomor_bulan - 1]
    print("\nBulan yang dipilih :", bulan_dipilih)

    for data in pembayaran:
        if data["nisn"] == siswa_ditemukan["nisn"] and data["bulan"] == bulan_dipilih:
            print("\nBulan", bulan_dipilih, "sudah dibayar!")
            return

    print()
    print("==============================")
    print("       PEMBAYARAN SPP")
    print("==============================")
    print("Siswa   :", siswa_ditemukan["nama"])
    print("Bulan   :", bulan_dipilih)
    print("Tagihan : Rp", NOMINAL_SPP)

    uang_bayar = input("Masukkan uang pembayaran: ")

    if not uang_bayar.isdigit():
        print("\nMasukkan jumlah uang dengan angka!")
        return

    uang_bayar = int(uang_bayar)

    if uang_bayar < NOMINAL_SPP:
        print("\nUang pembayaran tidak cukup!")
        print("Kekurangan : Rp", NOMINAL_SPP - uang_bayar)
        return

    kembalian = uang_bayar - NOMINAL_SPP

    pembayaran.append({
        "nisn": siswa_ditemukan["nisn"],
        "bulan": bulan_dipilih,
        "nominal": NOMINAL_SPP
    })

    print()
    print("==============================")
    print("   PEMBAYARAN BERHASIL")
    print("==============================")
    print("Siswa      :", siswa_ditemukan["nama"])
    print("Bulan      :", bulan_dipilih)
    print("Tagihan    : Rp", NOMINAL_SPP)
    print("Dibayar    : Rp", uang_bayar)
    print("Kembalian  : Rp", kembalian)