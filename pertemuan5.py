print("     GEROBAK FRIED CHICKEN        ")
print("----------------------------------")
print("Kode  jenis potong       Harga    ")
print("D      Dada              Rp.2500  ")
print("P      Paha              Rp.2000  ")
print("S      Sayap             Rp.1500  ")
print("----------------------------------")

#Input banyak jenis ayam yang dibeli
banyak_jenis = int(input("Banyak jenis : "))

#variable total bayar 
Total_bayar=0
Data_pesanan=[]

#proses input data pesanan 
for i in range(banyak_jenis):
    print(f"\njenis ke-{i+1}")
    kode = input ("kode potong [D/P/S]):").upper()
    banyak_potong = int(input("banyak potong :  "))
   
    if   kode=="D":
          jenis="Dada"
          harga=2500
    elif kode=="S":
          jenis="Sayap"
          harga=1500
    elif kode=="P":
          jenis="Paha"
          harga=2000
    else:
         print("tidak ada dalam menu")

jumlah = harga * banyak_potong
Total_bayar += jumlah
 
#simpan ke list
Data_pesanan.append([jenis, harga, banyak_potong, jumlah])

#hitungan pajak 10%
pajak = Total_bayar*0.10
Total_bayar_akhir =  Total_bayar + pajak  

#bentuk tampilan hasil 

print("\n-------------------------------------")
print("          GEROBAK FRIED CHICKEN        ")
print("---------------------------------------")

print("  No jenis potong   banyak jumlah      ")
print("---------------------------------------")

no = 1
for data in Data_pesanan:
    print("{:<3} {:<13} Rp{:<6} {:<7} Rp{}".format(no, data[0], data[1], data[2], data[3]))
    no += 1

print("-----------------------------------------")
print("Jumlah Bayar           Rp" + str(Total_bayar))
print("Pajak 10%              Rp" + str(int(pajak)))
print("Total Bayar            Rp" + str(int(Total_bayar_akhir)))
print("=========================================")
