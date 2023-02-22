while True:
    nama = input("Masukkan Nama Lengkap Anda: ")
    prodi = input("Masukkan Prodi Anda: ")
    nilai_huruf = input("Masukkan Nilai yang Anda Dapat: ")
    
    if nilai_huruf == 'A':
        nilai_angka = 4.0
        print(f"Nilai anda adalah {nilai_angka}, tbl tbl serem bgt lohh")
        break
    elif nilai_huruf == 'A-':
        nilai_angka = 3.75
        print(f"Nilai anda adalah {nilai_angka}, kamu keren!")
        break
    elif nilai_huruf == 'B+':
        nilai_angka = 3.25
        print(f"Nilai anda adalah {nilai_angka}, mulai ada peningkatan")
        break
    elif nilai_huruf == 'B':
        nilai_angka = 3.0
        print(f"Nilai anda adalah {nilai_angka}, ayo lebih semangat lagi")
        break
    elif nilai_huruf == 'B-':
        nilai_angka = 2.75
        print(f"Nilai anda adalah {nilai_angka}, kurang semangat belajar nihh")
        break
    elif nilai_huruf == 'C+':
        nilai_angka = 2.25
        print(f"Nilai anda adalah {nilai_angka}, perlu ditingkatkan")
        break
    elif nilai_huruf == 'C':
        nilai_angka = 2.0
        print(f"Nilai anda adalah {nilai_angka}, kamu perlu belajar lagi")
        break
    elif nilai_huruf == 'D':
        nilai_angka = 1.0
        print(f"Nilai anda adalah {nilai_angka}, apakah sudah ada pikiran untuk pindah jurusan?")
        break
    elif nilai_huruf == 'E':
        nilai_angka = 0
        print(f"Nilai anda adalah {nilai_angka}, niat kuliah nggak sih???")
        break
    else:
        print("Maaf, nilai huruf yang Anda masukkan tidak valid. Silakan coba lagi.")
