from pembayaran import NOMINAL_SPP, BULAN


def tampilkan_statistik(siswa, pembayaran):
    print()
    print("==============================")
    print("       STATISTIK SPP")
    print("==============================")

    if len(siswa) == 0:
        print("Belum ada data siswa.")
        return

    total_siswa = len(siswa)
    total_bulan_lunas = 0
    total_pemasukan = 0
    siswa_lunas_penuh = 0
    siswa_belum_bayar = 0
    siswa_menunggak = 0

    print()
    print("------------------------------")
    print("RINCIAN PER SISWA")
    print("------------------------------")

    for data_siswa in siswa:
        bulan_dibayar = []
        nominal_siswa = 0
        for data_bayar in pembayaran:
            if data_bayar["nisn"] == data_siswa["nisn"]:
                bulan_dibayar.append(data_bayar["bulan"])
                nominal_siswa += data_bayar["nominal"]

        bulan_lunas = []
        bulan_belum = []
        for bulan in BULAN:
            if bulan in bulan_dibayar:
                bulan_lunas.append(bulan)
            else:
                bulan_belum.append(bulan)

        jumlah_lunas = len(bulan_lunas)
        jumlah_belum = len(bulan_belum)

        if jumlah_lunas == 0:
            status = "BELUM PERNAH BAYAR"
            siswa_belum_bayar += 1
        elif jumlah_belum == 0:
            status = "LUNAS 12 BULAN"
            siswa_lunas_penuh += 1
        else:
            status = "MENUNGGAK"
            siswa_menunggak += 1

        total_bulan_lunas += jumlah_lunas
        total_pemasukan += nominal_siswa

        print("Nama      :", data_siswa["nama"])
        print("NISN      :", data_siswa["nisn"])
        print("Kelas     :", data_siswa["kelas"])
        print("Status    :", status)

        if jumlah_lunas > 0:
            print("Sudah bayar (", jumlah_lunas, "bulan ):", ", ".join(bulan_lunas))
        else:
            print("Sudah bayar : -")

        if jumlah_belum > 0:
            print("Belum bayar (", jumlah_belum, "bulan ):", ", ".join(bulan_belum))
            print("Tunggakan   : Rp", jumlah_belum * NOMINAL_SPP)
        else:
            print("Belum bayar : -")
        print("------------------------------")

    total_bulan_seharusnya = total_siswa * len(BULAN)
    total_tunggakan = total_bulan_seharusnya - total_bulan_lunas
    nilai_tunggakan = total_tunggakan * NOMINAL_SPP

    print()
    print("==============================")
    print("      RINGKASAN TOTAL")
    print("==============================")
    print("Total Siswa         :", total_siswa, "orang")
    print("Lunas 12 Bulan      :", siswa_lunas_penuh, "orang")
    print("Menunggak           :", siswa_menunggak, "orang")
    print("Belum Pernah Bayar  :", siswa_belum_bayar, "orang")
    print()
    print("Total Bulan Lunas   :", total_bulan_lunas, "bulan")
    print("Total Pemasukan     : Rp", total_pemasukan)
    print("Total Tunggakan     :", total_tunggakan, "bulan")
    print("Nilai Tunggakan     : Rp", nilai_tunggakan)
    print("==============================")