print("     GEROBAK FRIED CHICKEN        ")
print("----------------------------------")
print("Kode  jenis potong       Harga    ")
print("D      Dada              Rp.2500  ")
print("P      Paha              Rp.2000  ")
print("S      Sayap             Rp.1500  ")
print("----------------------------------")

#Input banyak jenis ayam yang dibeli
banyak = int(input("Banyak Jenis : "))
total = 0


#Input pesanan
for i in range(banyak):
    print("\nJenis ke-" + str(i+1))
    kode = input("Kode Potong [D/P/S] : ").upper()
    jumlah = int(input("Banyak Potong : "))

    if kode == "D":
        jenis, harga = "Dada", 2500
    elif kode == "P":
        jenis, harga = "Paha", 2000
    elif kode == "S":
        jenis, harga = "Sayap", 1500
    else:
        jenis="-"
        harga=0

    subtotal = harga * jumlah
    total += subtotal
    print(jenis + "  Rp" + str(harga) + " x " + str(jumlah) + " = Rp" + str(subtotal))

pajak = total * 0.10
total_akhir = total + pajak

print("\n=========================================")
print("Total Bayar : Rp" + str(total))
print("Pajak 10%   : Rp" + str(int(pajak)))
print("TOTAL AKHIR : Rp" + str(int(total_akhir)))
print("=========================================")
