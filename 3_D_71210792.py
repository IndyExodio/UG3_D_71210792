awal = int(input("Masukkan awal deret: "))
akhir = int(input("Masukkan ahkir deret: "))

print(" ".join(str(i) if i % 6 != 0 and i % 8 != 0 else "" for i in range(awal, akhir+1)))

