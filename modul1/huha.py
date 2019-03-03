def segitiga():
    n = int(input("Masukkan Tinggi segitiga : "))
    for i in range(0,n+1):
        print("*"*i)

def segitiga():
    n = int(input("Masukkan Tinggi Segitiga : "))
    for i in range(0,n):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")
segitiga()

def persegi():
    a = int(input("Masukkan Panjang : "))
    b = int(input("Masukkan Lebar : "))
    for i in range(b):
        if i == 0 or i == b-1:
            print("@"*b)
        else:
            print("@"+" "*(a-2)+"@")
persegi()


def vokal():
    a = "AIUEOaiueo"
    jmlvok = ""
    n = str(input("Masukkan Huruf Yang Akan dicek : "))
    for char in n:
        if char in a:
            jmlvok+=char
    s = len(jmlvok)
    print(s)
            
vokal()

def rata(huha):
    masukan =[]
    for d in huha:
        masukan.append(d)
    print(masukan)
    rerata = sum(masukan)/len(masukan)
    print("Hasilnya adalah ",rerata)
c = [2,2]        
rata(c)
