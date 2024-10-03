#Inputasi nilai N,r, dan c
N, r, c = map(int,input().split())

#Membuat matrix r kali c (baris kali kolom) dengan semua nilainya sama dengan nol
matrix = [[0 for _ in range(c)] for _ in range(r)]

#Memasukan siswa ke posisi yang ada di matrix
for i in range(N):
    j, k, l = map(int,input().split()) 
    matrix[(k - 1)][(l - 1)] = j

#Deklarasi array kosong "Sampingan" untuk menyimpan nilai siapa di samping siapa
sampingan = [0] * N

#Mencari siswa siapa di sampingnya
for m in range (0, r):
    for n in range(0, c):
        if matrix[m][n] != 0:
            if matrix[m][(n - 1)] > 0:
                sampingan[(matrix[m][n] - 1)] = matrix[m][(n - 1)]
            elif matrix[m][(n + 1)] > 0:
                sampingan[(matrix[m][n] - 1)] = matrix[m][(n + 1)]
            else:
                sampingan[(matrix[m][n] - 1)] = 0


    
#Memakai for loop untuk mengprint output satu per satu dalam array "sampingan"
for samping in sampingan:
    print(samping)









