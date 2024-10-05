#Melakukan inputasi r,c, dan N
r, c, N = map(int,input().split())

#Proses mengisi nilai petak hutan
petak = [list(map(int,input().split())) for _ in range (r)]

#Input pergerakan dengan karakter tanpa spasi sebanyak N digit
gerak = input() 

#Deklarasi variabel i dan j (sebagai penunjuk kolom dan baris) lalu variabel emas untuk menyimpan nilai emas
i = 0
j = 0
emas = petak[i][j]

#Melakukan looping untuk mengecek setiap pergerakan dan menghitung perubahan jumlah emas
for char in gerak:
    if char == 'R':
        j += 1
        if j > (c - 1):
            gerak = False 
            break
        emas += petak[i][j]
        emas += 3
        petak[i][j] = 0
    elif char == 'L':
        j -= 1
        if j < 0 :
            gerak = False
            break
        emas += petak[i][j]
        emas -= 2
        petak[i][j] = 0
    elif char == 'U':
        i -= 1
        if i < 0 :
            gerak = False
            break
        emas += petak[i][j]
        emas += 3
        petak[i][j] = 0
    elif char == 'D':
        i += 1
        if i > (r - 1):
            gerak = False
            break
        emas += petak[i][j]
        emas -= 2
        petak[i][j] = 0
    else:
        print("gerakan tidak dipahami")



#Proses untuk menampilkan output :
if gerak == False:
    print(emas)
    print("gerakanmu salah bung!")
else:
    print(emas)


    
        