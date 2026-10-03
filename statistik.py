from pembayaran import NOMINAL_SPP


def tampilkan_statistik(siswa, pembayaran):
    print()
    print("==============================")
    print("       STATISTIK SPP")
    print("==============================")

    total_siswa = len(siswa)
    total_transaksi = len(pembayaran)

    total_pemasukan = 0
    for data in pembayaran:
        total_pemasukan += data["nominal"]

    siswa_sudah_bayar = 0
    for data_siswa in siswa:
        for data_bayar in pembayaran:
            if data_siswa["nisn"] == data_bayar["nisn"]:
                siswa_sudah_bayar += 1
                break

    siswa_belum_bayar = total_siswa - siswa_sudah_bayar

    total_bulan_lunas = len(pembayaran)
    total_bulan_seharusnya = total_siswa * 12
    total_tunggakan = total_bulan_seharusnya - total_bulan_lunas
    nilai_tunggakan = total_tunggakan * NOMINAL_SPP

    print()
    print("------------------------------")
    print("DATA SISWA")
    print("------------------------------")
    print("Total Siswa       :", total_siswa, "orang")
    print("Siswa Sudah Bayar :", siswa_sudah_bayar, "orang")
    print("Siswa Belum Bayar :", siswa_belum_bayar, "orang")

    print()
    print("------------------------------")
    print("DATA PEMBAYARAN")
    print("------------------------------")
    print("Total Transaksi   :", total_transaksi, "transaksi")
    print("Total Pemasukan   : Rp", total_pemasukan)
    print("Total Bulan Lunas :", total_bulan_lunas, "bulan")

    print()
    print("------------------------------")
    print("DATA TUNGGAKAN")
    print("------------------------------")
    print("Total Tunggakan   :", total_tunggakan, "bulan")
    print("Nilai Tunggakan   : Rp", nilai_tunggakan)
    print("------------------------------")

    print()
    print("Statistik berhasil dihitung.")