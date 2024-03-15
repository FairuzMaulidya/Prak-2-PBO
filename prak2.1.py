# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:28:22 2024

@author: Fairuz Maulidya
"""

print("PROGRAM MENGHITUNG KELILING & LUAS SEGITIGA")

nama = input("Nama: ")
nim = input("NIM: ")

print("1. Keliling")
print("2. Luas")
pilihan = int(input("Masukan pilihan: "))

if pilihan == 1:
    sisi1 = float(input("Masukan sisi 1: "))
    sisi2 = float(input("Masukan sisi 2: "))
    sisi3 = float(input("Masukan sisi 3: "))
    keliling = sisi1 + sisi2 + sisi3
    print("Keliling Segitiga:", keliling, "cm")
else:
    alas = float(input("Masukan alas: "))
    tinggi = float(input("Masukan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga:", luas, "cm^2")
    
print("Terima kasih telah menggunakan program ini!")
