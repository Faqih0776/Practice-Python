jumlah_buku = 10
jumlah_buku_dibaca_dan_dipahami = 0
total_jumlah_baca = 0
print(f"jumlah buku yang sudah dibaca {jumlah_buku_dibaca_dan_dipahami}")
while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_dibaca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_dibaca_dan_dipahami = jumlah_buku_dibaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_dibaca_dan_dipahami} sudah dibaca dan dipahami")


print(f"jumlah buku yang sudah dibaca {jumlah_buku_dibaca_dan_dipahami}")