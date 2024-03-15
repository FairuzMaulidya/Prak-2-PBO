# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:38:43 2024

@author: Fairuz Maulidya
"""

class AngkaTercetak:
    def __init__(self, nim):
        self.dua_digit_terakhir_nim = int(nim[-2:])
        self.angka_tercetak = 0

    def cetak_angka(self):
        for i in range(1, 51):
            if i != self.dua_digit_terakhir_nim:
                print(i, end=" ")
                self.angka_tercetak += 1
                if self.angka_tercetak % 26 == 0:
                    print()  # Pindah ke baris baru

nim = input("Masukkan dua digit terakhir NIM Anda: ")

angka_tercetak = AngkaTercetak(nim)

angka_tercetak.cetak_angka()