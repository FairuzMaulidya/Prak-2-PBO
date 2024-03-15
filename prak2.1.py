# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:28:22 2024

@author: Fairuz Maulidya
"""

class Segitiga:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def hitung_keliling(self):
        sisi1 = float(input("Masukan sisi 1: "))
        sisi2 = float(input("Masukan sisi 2: "))
        sisi3 = float(input("Masukan sisi 3: "))
        return sisi1 + sisi2 + sisi3

    def hitung_luas(self):
        alas = float(input("Masukan alas: "))
        tinggi = float(input("Masukan tinggi: "))
        return 0.5 * alas * tinggi

    def tampilkan_menu(self):
        print("1. Keliling")
        print("2. Luas")

    def jalankan_program(self):
        print("PROGRAM MENGHITUNG KELILING & LUAS SEGITIGA")

        self.tampilkan_menu()
        pilihan = int(input("Masukan pilihan: "))

        if pilihan == 1:
            keliling = self.hitung_keliling()
            print("Keliling Segitiga:", keliling, "cm")
        else: 
            luas = self.hitung_luas()
            print("Luas Segitiga:", luas, "cm^2")

        print("Terima kasih telah menggunakan program ini!")


# Membuat instance dari class Segitiga
nama = input("Nama: ")
nim = input("NIM: ")
segitiga_calculator = Segitiga(nama, nim)

# Menjalankan program
segitiga_calculator.jalankan_program()

