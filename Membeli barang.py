#Membuat input jumlah barang (N) dan jumlah uang yang diberikan (M)
N, M = map(int,input().split())

#Melakukan inputasi nilai pada array
harga = list(map(int,input().split()))
jinah = list(map(int,input().split()))

#Deklarasi variabel untuk mengecek apakah semua positif atau semua negatif pada array harga dan jinah
#pos1 dan neg1 untuk mengecek array harga
pos1 = 0 
neg1 = 0
#pos2 dan neg2 untuk mengecek array jinah
pos2 = 0
neg2 = 0

#Deklarasi variabel bernama beli dan bayar
hbeli = 0
hbayar = 0

#Mengecek positif dan negatif dari array harga
for a in harga:
    if a >= 0:
        pos1 += 1 
    else:
        neg1 +=1

#Mengecek positif dan negatif dari array jinah
for b in jinah:
    if b >= 0:
        pos2 += 1 
    else:
        neg2 +=1

#Mencari optimasi harga barang terbesar dari array harga
if (pos1 == 0 and neg1 != 0) and (pos2 != 0 and neg2 == 0):
    print("0")

else:
    if (pos1 != 0 and neg1 != 0) or pos1 != 0:
        for i in harga:
            if i > 0: 
                hbeli += i
            else:
                hbeli += 0
    else:
        hbeli = max(harga)

    #Mencari optimasi pecahan uang terkecil dari array jinah
    if (pos2 != 0 and neg2 != 0) or neg2 != 0:
        for j in jinah:
            if j < 0:
                hbayar += j
            else:
                hbayar += 0
    else:
        hbayar = min(jinah)

    #Proses mengeluarkan output
    print(hbayar - hbeli)

