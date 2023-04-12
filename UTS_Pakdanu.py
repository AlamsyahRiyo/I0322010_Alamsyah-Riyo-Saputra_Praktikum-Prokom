harga_rumah = {'T 45/84':  550_000_000, 'T 55/112': 850_000_000, 'T 60/120': 950_000_000}


harga         = int(input("masukkan harga : "))
DP            = int(input("masukkan dp    : ")) 
rentang_tenor = int(input("masukkan tenor : "))


# deklarasikan suku
suku_bunga = 6/100

# Rentang pilihan tenor
rentang_tenor = range(1,12)

for tipe in harga_rumah:
    print(f"Tipe rumah {tipe}:")
    for tenor in rentang_tenor:
        pokok = harga_rumah[tipe] * (1 - 0)
        tenor_bulan = tenor * 12
        utang = (suku_bunga / 12) * pokok
        cicilan = ((utang * pokok) * tenor) / tenor_bulan
        uang_pertama = pokok
        
        print(f"Tenor {tenor} tahun: uang pertama  {uang_pertama:,} dan cicilan {int(cicilan):,}")



        