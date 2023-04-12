harga              = float(input("Harga rumah (dalam rupiah)= "))
uang_muka          = float(input("Uang muka (dalam rupiah): "))
tenor              = int(input("Tenor (dalam tahun): "))
suku_bunga_bulanan = 0.5

# Rumus menghitung besar cicilan dan besar hutang
besar_hutang = harga - uang_muka
cicilan_pokok_bulanan = besar_hutang / (tenor * 12)
cicilan_bunga_bulanan = besar_hutang * suku_bunga_bulanan
total_cicilan_bulanan = cicilan_pokok_bulanan + cicilan_bunga_bulanan

#menghitung besar total pembayaran
biaya_notaris    = 2000000
biaya_provisi    = 1500000
pajak_pembelian  = harga * 0.025
pnbp             = 650000
biaya_balik_nama = 1500000
total_pembayaran_pertama = uang_muka +harga + total_cicilan_bulanan + biaya_notaris + biaya_provisi + pajak_pembelian + pnbp + biaya_balik_nama


print("====================Jumlah yang harus dibayarkan oleh Anda Sebesar===================")
print("Besar hutang         = Rp", round(besar_hutang,))
print("Cicilan pokok bulanan= Rp", round(cicilan_pokok_bulanan,))
print("Cicilan bunga bulanan= Rp", round(cicilan_bunga_bulanan,))
print("Total cicilan bulanan= Rp", round(total_cicilan_bulanan,))
print("biaya notaris        = Rp", round(biaya_notaris,))
print("biaya provisi        = Rp", round(biaya_provisi,))
print("pnbp                 = Rp", round(pnbp,))
print("biaya balik nama     = Rp", round(biaya_balik_nama,))
print("Total pembayaran     = Rp", round(total_pembayaran_pertama,))
print("=====================================================================================")
