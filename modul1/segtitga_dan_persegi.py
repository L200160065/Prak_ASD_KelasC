#modul 1 no 1 dan 2 

#persegi
# def segitiga():
#     a = int(input("Masukkan tinggi bintang : "))
#     for i in range(0,a):
#         for j in range(i+1):
#             print("*",end="")
#         print("\r")
# segitiga()

# def persegi():
#     a = int(input("Masukkan tinggi persegi : "))
#     b = int(input("Masukkan lebar persegi : "))
#     for i in range(b):
#         if i == 0 or i == b-1:
#             print("@"*b)
#         else:
#             print("@"+" "*(a-2)+"@")

# persegi()

# def jumlahHurufVokal(jmlvokal):
#     d = 'AIUEOaiueo'
#     jmlvok = ""
#     for char in jmlvokal:
#         if char in d:
#             jmlvok+=char
#     pan = len(jmlvok)
#     print(pan)
# jumlahHurufVokal("Anak Ini Enak")

# def jumlahHurufKonsonan(jmlkon):
#     d = "BCDFGHIJKLMNPQRSTVWXYZbcdfghijklmnpqrstvwxyz"
#     jmlkons = ""
#     for char in jmlkon:
#         if char in d:
#             jmlkons+=char
#     pan = len(jmlkons)
#     print(pan)

# jumlahHurufKonsonan("Xx")


# def rata(huha):
#     masukan =[]
#     for d in huha:
#         masukan.append(d)
#     print(masukan)
#     rerata = sum(masukan)/len(masukan)
#     print("Hasilnya adalah ",rerata)
# c = [1,2,3,4,5]        
# rata(c)


# def apakahTerkandung():
#     inputan = str(input("Masukkan kata : "))
#     cek_kata = str(input("kata yang akan dicari : "))
#     if cek_kata in inputan:
#         print(True)
#     else:
#         print(False)

# apakahTerkandung()

def faktorPrima(x):
    for i in range(1,x+1):
        if x == i:
            return[i]
        elif x%i ==0:
            x = float(x/i)
            return[i]+faktorPrima(x)
faktorPrima(22)

# def kelipatan():
#     a = "Python"
#     b = "Ums"
#     i = 1
#     while i <= 100:
#         if i % 3  == 0 and i % 5 == 0:
#             print (a,b)
#             i+=1
#         elif i%3 == 0:
#             print(a)
#             i+=1
#         elif i%5 == 0:
#             print(b)
#             i+=1
#         else:
#             print(i)
#             i+=1
# kelipatan()


# def kabisat():
#     tahun  = int(input("Tahun Kabisat : "))
#     if tahun % 4 == 0:
#         if tahun % 100 == 0:
#             if tahun % 400 == 0:
#                 print("Tahun Kabisat")
#             else:
#                 print ("Bukan Tahun Kabisat")
#         else:
#             print ("Tahun Kabisat")
#     else:
#         print ("Bukan Tahun Kabisat")

# kabisat()
         
# def tebak_angka():
#     angka =100
#     print("Permainan Tebak Angka")
#     print("Saya menyimpan sebuah angka bulat antara 1 sampai 100.Coba Tebak")
#     tebak = int(input("Masukkan Tebakan : "))
#     while(tebak!=angka):
#         if tebak <=100 and tebak >=90:
#             print("Itu Terlalu besar")
#             tebak = int(input("Masukkan Tebakan : "))
#         elif tebak <=50 :
#             print("Itu terlalu kecil")
#             tebak = int(input("Masukkan Tebakan : "))
#         elif tebak >=50 and tebak <=70 :
#             print("Yapp Anda Benar")
#             break
# tebak_angka()

def prima():
    batas_bawah=(int(input("Masukkan batas bawah bilangan yang ingin di review : ")))
    faktorial=0
    for b in range(2,batas_bawah+1):
        for c in range(2,b+1):
            cek = b%c
            if(cek is 0):
                faktorial +=1

        if(faktorial is 1):
            print(b," bilangan prima")
        else:
            print(b," bukan bilangan prima")
        faktorial = 0
prima()

# def apakahPrima(n):
#     from math import sqrt as sq
#     n = int(n)
#     assert n>0
#     primaKecil = [2,3,4,5,7,11]
#     bukanPrKecil = [0,1,4,6,8,9,10]
#     if n in primaKecil:
#         return True
#     elif n in bukanPrKecil:
#         return False
#     else :
#         for i in range(2,int(sq(n))+1):

# Nomor 13
# angka = {1: "satu", 2: "dua", 3: "tiga", 4: "empat", 5: "lima", 6: "enam", 7: "tujuh", 8: "delapan", 9: "sembilan"}
# b = ' puluh '
# c = ' ratus '
# d = ' ribu '
# e = ' juta '
# f = ' milyar '
# g = ' triliun '
# def katakan(x):
#     y = str(x)
#     n = len(y)
#     if n<=3:
#         if n ==1:
#             if y == '0':
#                 return ''
#             else:
#                 return angka[int(y)]
#         elif n == 2:
#             if y[0] == '1':
#                 if y[1] == '1':
#                     return 'sebelas'
#                 elif y[0] == '0':
#                     x = y[1]
#                     return katakan(x)
#                 elif y[1]:
#                     return 'sepuluh'
#                 else:
#                     return angka[int(y[1])] + ' belas '
#             elif y[0] == '0':
#                 x = y[1]
#                 return katakan(x)
#             else:
#                 x = y[1]
#                 return angka[int(y[0])] + b + katakan(x)
#         else:
#             if y[0] == '1':
#                 x = y[1:]
#                 return 'seratus ' + katakan(x)
#             elif y[0] == '1':
#                 x = y [1:]
#                 return katakan(x)
#             else:
#                 x = y[1:]
#                 return angka[int(y[0])] + c + katakan(x)
#     elif 3 < n<=6:
#         p = y[-3:]
#         q = y[:-3]
#         if q == '1':
#             return 'seribu ' +katakan(p)
#         elif q == '000':
#             return katakan(p)
#         else:
#             return katakan(q) + d +katakan(p)
#     elif 6 <n<=9:
#         r = y[-6:]
#         s = y[:-6]
#         return katakan(s) +e+katakan(r)
#     elif 9 < n <=12:
#         t = y[-9:]
#         u = y[:-9]
#         return katakan(u) + f + katakan(t)
#     else:
#         v=y[-12:]
#         w=y[:-12]
#         return katakan(w) + g + katakan(v)

# katakan(91029102)


##No. 14 formatRupiah
# def formatrupiah(uang):
#     y = str(uang)
#     if len(y) <=3:
#         return 'Rp' +y
#     else:
#         p = y[-3:]
#         q = y[:-3]
#         return formatrupiah(q)+'.'+p
#         return 'Rp '+formatrupiah(q)+'.'+p
     
# formatrupiah(1900)


# def faktorPrima(x):
#     faktor = []
#     ulang  = 2
#     while ulang <= x:
#         if x % ulang == 0:
#             x/=ulang
#             faktor.append(ulang)
#         else:
#             ulang+=1
#     return faktor

# m = int(input("Masukkan Angka  :  "))
# print(faktorPrima(m))
