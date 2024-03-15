# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:38:43 2024

@author: Fairuz Maulidya
"""

nim = input("Masukkan dua digit terakhir NIM Anda: ")
dua_digit_terakhir_nim = int(nim[-2:])

angka_tercetak = 0

for i in range(1, 51):
    if i != dua_digit_terakhir_nim:
        print(i, end=" ")
        angka_tercetak += 1
        # Cek apakah sudah mencapai 26 angka per baris
        if angka_tercetak % 26 == 0:
            print()  # Pindah ke baris baru

