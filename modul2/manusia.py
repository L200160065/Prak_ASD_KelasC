class Manusia(object):
    """"Class Manusia dengan inisiasi nama"""
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku",self.nama)
    def makan(self,s):
        print("Saya baru saja makan",self.s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan",k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2

p1 = Manusia("Fatimah")
p1.ucapkanSalam()

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ', NIM ' + str(self.NIM)\
            + ' Tinggal Di ' + self.kotaTinggal \
            + ' Uang Saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalai makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,tinggal):
        tinggal = self.kotaTinggal
        return self.kotaTinggal
    def ambahUangSaku(self,tambahuang):
        uangtambah = self.uangSaku + tambahuang
        return uangtambah
    def tambahmhasiswa(self):
        self.nama = str(input("Masukkan Nama Mahasiswa  : "))
        self.NIM = str(input("Masukkan NIM Mahasiswa : "))
        self.kotaTinggal = str(input("Masukkan Kota Domisili Mahasiswa : "))
        print(self.nama)
        print(self.NIM)
        print(self.kotaTinggal)
    def listkuliah(self):
        listkul = []
        
m1 = Mahasiswa('Jamil',234,'Surakarta',250000)
m1.ambilNama()
m1.tambahmhasiswa()

# class Pesan(object):
#     """Sebuah class bernama Pesan. Untuk memahami konsep Class dan Object"""
#     def __init__(self,sebuahString):
#         self.teks = sebuahString
#     def cetakIni(self):
#         print(self.teks)
#     def cetakPakaiHurufKapital(self):
#         print(str.upper(self.teks))
#     def cetakkPakaiHurufKecil(self):
#         print(str.lower(self.teks))
#     def jumKar(self):
#         return len(self.teks)
#     def cetakJUmlahKarakterku(self):
#         print("Kalimatku mempunyai",len(self.teks), ' karakter')
#     def perbarui(self,stringBaru):
#         self.teks = stringBaru
#     def apakahTerkandung(self,cekkata):
#         if cekkata in self.teks:
#             print(True)
#         else:
#             print(False)
#     def hitungKonsonan(self):
#         konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
#         jmlkonsonan = ""
#         for kons in self.teks:
#             if kons in konsonan:
#                 jmlkonsonan+=kons
#         pan = len(jmlkonsonan)
#         return pan
#     def hitungVokal(self):
#         vokal = 'AIUEOaiueo'
#         jmlvokal = ""
#         for voks in self.teks:
#             if voks in vokal:
#                 jmlvokal+=kons
#         pan = len(jmlvokal)
#         return pan

# pesanA = Pesan("Makan enak nih")
# pesanA.cetakIni()
# pesanA.cetakPakaiHurufKapital()
# pesanA.apakahTerkandung("Huh")