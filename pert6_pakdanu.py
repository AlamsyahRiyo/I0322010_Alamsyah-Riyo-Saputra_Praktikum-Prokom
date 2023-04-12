bunga = ("anggrek dendra", "anggrek bulan", "anggrek ekor tupai", "anggrek golden shower", "anggrek katlya")

def tampil_data ():
    print ("daftar bunga yang ada ")
    if len(bunga)==0:
        print(" belum ada data bunga ")
    else :
        for indeks in range(0,len(bunga)):
            print("no =", indeks," ", bunga[indeks])


# fungsi untuk masukkan data baru

def insert_data():
    bunga_baru = input("masukan nama bunga baru = ")
    bunga.append(bunga_baru)
    tampil_data()

#program utama data base

print("====Selamat datang di prog data base ====")
print()

print(' [1] Tampilkan data bunga ')
print(' [2] masukan   data bunga ')
print(' [3] menghapus data bunga ')

print()
print("========================================")

pilih = input("masukkan pilihan menu = ")
print("pilihan anda adalah           = ", pilih)

if pilih == "1":
    tampil_data()
if pilih == "2":
    insert_data()