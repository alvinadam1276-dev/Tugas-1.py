print("        PROGRAM HITUNG GAJI KARYAWAN      ")

nama = input("Nama Karyawan        : ")
golongan = int(input("Golongan Jabatan (1/2/3) : "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1) : ").upper()
jam_kerja = int(input("Jumlah jam kerja     : "))


gaji_pokok = 300000

if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid!")

if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid!")

if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * 3500
else:
    honor_lembur = 0

total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

print("\n==========================================")
print("               HASIL PERHITUNGAN          ")
print("==========================================")
print("Karyawan yang bernama : " + nama)
print("Honor yang diterima :")
print("  Tunjangan Jabatan      Rp " + str(int(tunjangan_jabatan)))
print("  Tunjangan Pendidikan   Rp " + str(int(tunjangan_pendidikan)))
print("  Honor Lembur           Rp " + str(int(honor_lembur)))


print("Total Gaji (Pokok + Tunjangan + Lembur)")
print("= Rp " + str(int(total_gaji)))
