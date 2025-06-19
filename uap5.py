from termcolor import colored, cprint
import os
import time

os.system('cls')  

obat_db = {
    "001": {"nama": "Paracetamol", "harga": 5000},
    "002": {"nama": "Amoxicillin", "harga": 8000},
    "003": {"nama": "Vitamin C  ", "harga": 6000},
    "004": {"nama": "Antasida   ", "harga": 4000},
    "005": {"nama": "Ibuprofen  ", "harga": 7000},
    "006": {"nama": "Cetirizine ", "harga": 6500},
    "007": {"nama": "Betadine   ", "harga": 9000},
    "008": {"nama": "Loperamide ", "harga": 4500},
    "009": {"nama": "Salep Kulit", "harga": 8500},
    "010": {"nama": "Zinc Tablet", "harga": 5500}
}

def input_angka():
    angka = input()
    while angka.isnumeric() == False:
        cprint("Input harus angka!", "red")
        angka = input()
    return int(angka)

def tampilkan_obat():
    cprint("===== DAFTAR OBAT =====", "cyan")
    for kode in obat_db:
        print(kode + " - " + obat_db[kode]["nama"] + " : Rp" + str(obat_db[kode]["harga"]))
    print("000 - [SELESAI INPUT]\n")

def input_obat():
    keranjang = []
    tampilkan_obat()
    while True:
        kode = input("Kode obat (000 untuk selesai): ")
        if kode == "000":
            return keranjang
        if kode in obat_db:
            jumlah = input("Masukkan jumlah: ")
            while not jumlah.isnumeric():
                cprint("Jumlah harus angka!", "red")
                jumlah = input("Masukkan jumlah: ")
            keranjang.append([kode, obat_db[kode]["nama"], int(jumlah), obat_db[kode]["harga"]])
        else:
            cprint("Kode tidak ditemukan!", "red")

def hitung_total(keranjang):
    total = 0
    for item in keranjang:
        total += item[2] * item[3]
    return total

def simpan_struk(keranjang, total, bayar, kembali):
    file = open("struk_apotek.txt", "w")
    file.write("===== STRUK PEMBELIAN =====\n")
    for item in keranjang:
        file.write(item[1] + " x " + str(item[2]) + " = Rp" + str(item[2] * item[3]) + "\n")
    file.write("\nTotal     : Rp" + str(total))
    file.write("\nBayar     : Rp" + str(bayar))
    file.write("\nKembalian : Rp" + str(kembali))
    file.close()
    cprint("Struk telah disimpan ke 'struk_apotek.txt'", "green")

def cetak_struk(keranjang, total, bayar, kembali):
    cprint("\n===== STRUK PEMBELIAN =====", "white", "on_magenta")
    for item in keranjang:
        subtotal = item[2] * item[3]
        warna = "red" if subtotal >= 10000 else "white"
        print(colored(item[1] + " x " + str(item[2]) + " = Rp" + str(subtotal), warna))
        time.sleep(0.3)
    cprint("\nTotal     : Rp" + str(total), "yellow")
    cprint("Bayar     : Rp" + str(bayar), "green")
    cprint("Kembalian : Rp" + str(kembali), "cyan")
    print()

def apotek():
    keluar = False
    while keluar == False:
        os.system('cls')
        cprint("===== SELAMAT DATANG DI APOTEK SEHAT =====", "blue")
        print("1. Mulai Pembelian Obat")
        print("2. Keluar")
        menu = input("Pilih menu: ")
        if menu == "1":
            os.system('cls')
            keranjang = input_obat()
            if len(keranjang) == 0:
                cprint("Keranjang kosong, tidak ada pembelian.", "yellow")
            else:
                total = hitung_total(keranjang)
                cprint("Total belanja: Rp" + str(total), "yellow")

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
                cetak_struk(keranjang, total, bayar, kembali)
                simpan_struk(keranjang, total, bayar, kembali)
                cprint("Tekan ENTER untuk kembali ke menu utama...", "cyan")
                input()
        elif menu == "2":
            cprint("Terima kasih telah berbelanja di Apotek Sehat!", "green")
            keluar = True
        else:
            cprint("Menu tidak valid!", "red")
            time.sleep(1)

apotek()