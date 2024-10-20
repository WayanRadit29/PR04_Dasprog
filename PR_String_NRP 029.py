#Tugas Implementasi string ada di bawah 

#Proses Deklarasi variabel dan nilainya dalam tipe data string
string_0 = "Wayan Raditya Putra"
string_1 = "5054241029"
string_2 = "Bali"

#Proses print string sesuai deklarasi variabel
print(f"Nama saya adalah {string_0}")
print(f"NRP saya adalah {string_1}")
print(f"Asal saya dari {string_2}")

#Acces suatu karakter di string
print(f"Inisial saya yaitu {string_0[0]}{string_0[6]}{string_0[14]}")

#Proses string slicing
print(f"Nama belakang saya adalah {string_0[-5:]}")
print(f"Nama panggilan saya adalah {string_0[0:5]}")

#Invers string
print(f"Reverse NRP saya adalah {string_1[::-1]}")

#Update string
string_3 = "Saya mahasiswa RKA"
string_3 = list(string_3)

list1 = list(string_3)
list1[5:] = "bukan mahasiswa RPL"
string_4 = ''.join(list1)
print(string_4)

# #Tugas Implementasi 

#Deleting a character dari kota asal

string_2del = list(string_2)
string_2del[1] = ''
hasil = ''.join(string_2del)
print(hasil)

#Escape sequencing in python

#Initial String
escape1 = """Rendi pun membalas, "Halo Wayan, salam kenal" """
print(escape1)

#Escaping Single Quote
escape2 = 'He doesn\'t read book everday'
print(escape2)

#Escaping Double Quotes
escape3 = "Wayan pun berkata, \"Hai saya Wayan Raditya Putra\""
print(escape3)

#Escaping Backslashes
escape4 = "C:\\Users\\Wayan\\Documents\\"
print("\nEscaping Backslashes: ")
print(escape4)

#Use of Tab
escape5 = "Wayan\tRaditya\tPutra"
print("\nTab: ")
print(escape5)

#Use of New Line
escape6 = "Saya Wayan\nMahasiswa AI ITS"
print("\nNew Line: ")
print(escape6)

#Ignore Sequence
#Printing Bali in octal
notescape1 = "\102\141\154\151"
print(notescape1)

#Using raw String to ignore Escape Sequences
notescape2 = r"This is \102\141\154\151"
print(notescape2)

#Printing Ubud in HEX
notescape3 = "This is \x55\x62\x75\x64 in \x42\x41\x4c\x49"
print(notescape3)

#Using raw String to ignore Escape Sequences
notescape4 = r"This is \x55\x62\x75\x64 in \x42\x41\x4c\x49"
print(notescape4)




#Python string formating

#Default order
format1 = "{} {} {}".format('AI', 'ITS', '2024')
print(format1)

#Positional Formatting
format2 = "{1} {0} {2}".format('Institut Teknologi Sepuluh Nopember', 'Keren', 'AI')
print(format2)

#Keyword Formatting
format3 = "{its} {year} {institute}".format(its='ITS', year='2024', institute='Teknologi Sepuluh Nopember')
print(format3)

#Formatting of Integers
format4 = "{0:b}".format(42)
print(format4)

#Formatting of Floats
format5 = "{0:e}".format(123.4567)  
print(format5)

#Rounding off Integers
format6 = "{0:.2f}".format(2/7) 
print(format6)

#String alignment
format7 = "|{:<10}|{:^10}|{:>10}|".format('Gravitasi', 
                                          'ditemukan', 
                                          'Newton')
print(format7)

#To demonstrate aligning of spaces
format8 = "\n{0:^16} ditemukan pada tahun {1:<4}!".format("Gravitasi",
                                                    1687)
print(format8)


#Old Style Formatting of integer
bilangan_bulat = 121.21212  
print('Nilai bilangan_bulat adalah %3.2f' % bilangan_bulat)
print('Nilai bilangan_bulat adalah %3.4f' % bilangan_bulat)




