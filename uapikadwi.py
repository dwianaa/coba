from termcolor import colored, cprint
import os
import time

obat_db = {
    "001": {"nama": "Paracetamol", "harga": 5000},
    "002": {"nama": "Amoxicillin", "harga": 8000},
    "003": {"nama": "Vitamin C", "harga": 6000},
    "004": {"nama": "Antasida", "harga": 4000},
    "005": {"nama": "Ibuprofen", "harga": 7000},
    "006": {"nama": "Cetirizine", "harga": 6500},
    "007": {"nama": "Betadine", "harga": 9000},
    "008": {"nama": "Loperamide", "harga": 4500},
    "009": {"nama": "Salep Kulit", "harga": 8500},
    "010": {"nama": "Zinc Tablet", "harga": 5500}
}

def loading_animation(teks="Memuat...", durasi=2):
    for i in range(durasi * 4):
        titik = "." * (i % 4)
        print(f"\r{teks}{titik}", end='')
        time.sleep(0.25)
    print()

def animasi_struk():
    cprint("\nMencetak struk", "green")
    for i in range(5):
        print(colored("█" * (i + 1), "white", "on_green"), end='\r')
        time.sleep(0.2)
    print(colored("█ Selesai!", "green", "on_black"))

def opening_banner():
    os.system('cls')
    cprint("="*35, "magenta")
    cprint("      SELAMAT DATANG DI", "magenta", attrs=['bold'])
    cprint("    APLIKASI KASIR APOTEK SEHAT", "magenta", attrs=['bold'])
    cprint("="*35, "magenta")
    loading_animation("Menyiapkan aplikasi")
    os.system('cls')

def tampilkan_obat():
    cprint("\n===== DAFTAR OBAT =====", "cyan")
    for kode in obat_db:
        nama = obat_db[kode]["nama"]
        harga = obat_db[kode]["harga"]
        print(f"{kode} - {nama:<15} : Rp{harga}")
    print("000 - [SELESAI INPUT]")

def input_pembelian():
    keranjang = []
    tampilkan_obat()
    while True:
        kode = input("\nMasukkan kode obat (000 untuk selesai): ")
        if kode == "000":
            break
        if kode in obat_db:
            jumlah = input("Masukkan jumlah: ")
            while not jumlah.isdigit():
                cprint("Jumlah harus berupa angka!", "red")
                jumlah = input("Masukkan jumlah: ")
            jumlah = int(jumlah)
            data = obat_db[kode]
            keranjang.append([data["nama"], jumlah, data["harga"]])
        else:
            cprint("Kode tidak ditemukan!", "red")
    return keranjang

def hitung_total(keranjang):
    total = 0
    for item in keranjang:
        total += item[1] * item[2]
    return total

def simpan_data(nama, keranjang, total):
    with open("data_pembelian.txt", "a") as file:
        for item in keranjang:
            file.write(f"{nama}, {item[0]}, {item[1]}, {item[2]*item[1]}\n")
    cprint("Data pembelian telah disimpan.", "green")

def simpan_struk(keranjang, total, bayar, kembali):
    with open("struk_apotek.txt", "a") as file:
        file.write("\n=============================\n")
        file.write("        STRUK PEMBELIAN\n")
        file.write("=============================\n")
        for item in keranjang:
            nama_obat = item[0]
            jumlah = item[1]
            harga_satuan = item[2]
            subtotal = jumlah * harga_satuan
            file.write(f"Nama Obat : {nama_obat}\n")
            file.write(f"Jumlah    : {jumlah}\n")
            file.write(f"Harga     : Rp{harga_satuan}\n")
            file.write(f"Subtotal  : Rp{subtotal}\n")
            file.write("-----------------------------\n")
        file.write(f"TOTAL     : Rp{total}\n")
        file.write(f"BAYAR     : Rp{bayar}\n")
        file.write(f"KEMBALIAN : Rp{kembali}\n")
        file.write("=============================\n")
    cprint("Struk telah disimpan ke 'struk_apotek.txt'", "green")

def cetak_struk(keranjang, total, bayar, kembali):
    cprint("\n===== STRUK PEMBELIAN =====", "white", "on_magenta")
    for item in keranjang:
        nama_obat = item[0]
        jumlah = item[1]
        harga_satuan = item[2]
        subtotal = jumlah * harga_satuan
        print(f"{nama_obat} x {jumlah} = Rp{subtotal}\n")
    cprint("\nTotal     : Rp" + str(total), "yellow")
    cprint("Bayar     : Rp" + str(bayar), "green")
    cprint("Kembalian : Rp" + str(kembali), "cyan")
    print()

def tampilkan_data_pembelian():
    print("\n================= DATA PEMBELIAN =================")
    try:
        with open("data_pembelian.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        cprint("File data belum tersedia.", "red")
        return
    if not lines:
        cprint("Belum ada data pembelian.", "yellow")
        return
    print(f"{'Nama':<15} {'Obat':<15} {'Jumlah':<7} {'Total Harga':<12}")
    print("="*50)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            nama, obat, jumlah, total = parts
            print(f"{nama:<15} {obat:<15} {jumlah:<7} Rp{total:<10}")

def hapus_data(nama_hapus):
    try:
        with open("data_pembelian.txt", "r") as file:
            lines = file.readlines()
        with open("data_pembelian.txt", "w") as file:
            for line in lines:
                if line.split(",")[0].strip() != nama_hapus:
                    file.write(line)
        cprint(f"Data atas nama {nama_hapus} telah dihapus (jika ada).", "red")
    except FileNotFoundError:
        cprint("File data belum tersedia.", "red")

def main():
    opening_banner()
    while True:
        cprint("\n=== APLIKASI KASIR APOTEK SEHAT ===", "blue")
        print("1. Mulai Pembelian Obat")
        print("2. Tampilkan Data Pembelian")
        print("3. Hapus Data Pembelian")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            loading_animation("Mempersiapkan transaksi")
            nama = input("\nMasukkan nama Anda: ")
            keranjang = input_pembelian()
            if keranjang:
                total = hitung_total(keranjang)
                cprint(f"\nTotal yang harus dibayar: Rp{total}", "yellow")

                uang_sah = ["1000", "2000", "5000", "10000", "20000", "50000", "100000"]
                bayar = 0
                cprint("Masukkan uang pecahan satu per satu (contoh: 10000)", "cyan")
                while bayar < total:
                    print(f"Total dibayar sementara: Rp{bayar} / Rp{total}")
                    lembar = input("Masukkan uang: ")
                    if lembar in uang_sah:
                        bayar += int(lembar)
                    else:
                        cprint("Pecahan tidak valid. Gunakan pecahan sah!", "red")

                kembali = bayar - total
                simpan_data(nama, keranjang, total)
                animasi_struk()
                simpan_struk(keranjang, total, bayar, kembali)
                cetak_struk(keranjang, total, bayar, kembali)
            else:
                cprint("Tidak ada pembelian dilakukan.", "yellow")
        elif pilihan == "2":
            tampilkan_data_pembelian()
        elif pilihan == "3":
            nama = input("Masukkan nama yang ingin dihapus datanya: ")
            hapus_data(nama)
        elif pilihan == "4":
            cprint("Terima kasih telah menggunakan Apotek Sehat!", "cyan")
            break
        else:
            cprint("Pilihan tidak valid!", "red")
        input("\nTekan ENTER untuk kembali ke menu... ")
        os.system('cls')

main()   