#Input nilai N dan K
N, K = map(int,input().split())

#Membuat list bernama harga_buah
harga_buah = list(map(int,input().split()))

#deklarasi variabel bernama kombinasi 
kombinasi = 0

#Melakukan pengecekan kombinasi dengan for loop
for i in harga_buah:
    if i <= K:
        kombinasi += 1
    else:
        kombinasi += 0

#print out total kombinasi
print(kombinasi)

