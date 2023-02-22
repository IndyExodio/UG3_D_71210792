try:
    plat_nomor = input("Masukkan Plat Nomor : ")
    nomor = int(plat_nomor.split()[1])
    if 0 <= nomor <= 3000:
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif 3001 <= nomor <= 4000:
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif 4001 <= nomor <= 5000:
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")
    else:
        print("Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode daerah")
except:
    print("Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode daerah")
