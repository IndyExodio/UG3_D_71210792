curah_hujan = float(input("Masukkan nilai curah hujan: "))
kondisi_cuaca = "Cuaca Terang/Berawan" if curah_hujan == 0 else "Curah hujan ringan" if 0.5 <= curah_hujan <= 20 else "Curah hujan sedang" if 21 <= curah_hujan <= 50 else "Curah hujan lebat" if 51 <= curah_hujan <= 100 else "Curah hujan ekstrem" if curah_hujan > 100 else "Input tidak valid"
print(kondisi_cuaca)