import sqlite3

import models


class Urun:
    db = sqlite3.connect('MyDb.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS urun (urunAdi TEXT, urunFiyat INTEGER, urunTuru TEXT, urunID INTEGER)")

    urunAdi = ""
    urunID = 0
    urunFiyat = 0
    urunTuru = ""

    def __init__(self, urunAdi, urunFiyat, urunTuru, urunID):
        self.urunAdi = urunAdi
        self.urunFiyat = urunFiyat
        self.urunTuru = urunTuru
        self.urunID = urunID

    def __init__(self, urunAdi, urunFiyat, urunTuru):
        self.urunAdi = urunAdi
        self.urunFiyat = urunFiyat
        self.urunTuru = urunTuru


    def urunKayit(self, urun):

        db = sqlite3.connect("MyDb.db")
        cursor = db.cursor()

        try:
            command = "insert into urun(urunAdi,urunFiyat,urunTuru, urunID) values (?,?,?,?)"
            cursor.execute(command, (urun.urunAdi, urun.urunFiyat, urun.urunTuru, urun.urunID))
            db.commit()
            print("KAYIT BAŞARILI", "Kayıt tamamlanmıştır.")
            db.close()
        except:
            print("HATA", "Veritabanına kayıt sırasında hata oluştu.")
            db.close()



    def getUrun(self):

        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = """SELECT urunID, urunAdi, urunFiyat, urunTuru FROM Urun"""
        cursor.execute(command)
        i = cursor.fetchall()
        for x in i:
            print(x)


    def getSeciliUrun(self):
        sepet = models.sepet.Sepet
        kontrol = 0
        urunTuru = input("Hangi türde ürün almak istiyorsunuz?(araba , çikolata, gofret, uçak, vb.)")
        print()
        print("urunID, urunAdi, urunFiyat, urunTuru")
        print("------  -------  ---------  --------")
        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = """SELECT  urunID, urunAdi, urunFiyat, urunTuru FROM urun"""
        cursor.execute(command)
        i = cursor.fetchall()
        for x in i:
                if(x[3] == urunTuru):
                    print(x)
                    kontrol = 1

        if(kontrol == 0):
            print("Girdiğiniz ürün türünde ürün bulunamamıştır!!!!!!!!!!!")
        else:
            sepet.sepeteEkle(sepet)

    def getSeciliUrunList(self):

        sepet = models.sepet.Sepet
        urun = models.urun.Urun
        print()
        urunID = (input("Sepete eklemek istediğiniz ürünün ID'sini giriniz: "))

        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = """SELECT  urunID, urunAdi, urunFiyat, urunTuru FROM urun"""
        cursor.execute(command)
        i = cursor.fetchall()
        for x in i:
            if (x[0] == int(urunID)):
                urun1 = urun(x[1], x[2], x[3])
                sepet.sepetList.append(urun1)
                sepet.sepetFiyat = sepet.sepetFiyat + x[2]
                print("Ürün sepete başarıyla eklenmiştir!!!!!!!!!!")
            else:
                pass